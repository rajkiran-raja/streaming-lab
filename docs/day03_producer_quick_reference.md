# Day 3 Quick Reference: Python Producer

Status: Day 3 complete. Run all commands from `/workspaces/streaming-lab`.

---

## 1. Mental model: the post office

1. `produce()` puts the message in an **outbox** inside your program. It sends nothing and runs no callback.
2. A background **courier** ships batches to Kafka. Kafka stores them and sends a **receipt** (ack = "I stored it").
3. Receipts wait in a pile. `poll()` or `flush()` reads them, and that is when your `done` callback runs.
4. `flush()` waits until the outbox is empty and every receipt is read.

| Call | What it does |
|---|---|
| `produce()` | Queue a message in the outbox |
| `poll(0)` | Read receipts that already arrived, then move on (never waits) |
| `flush()` | Wait until everything is stored and every receipt is read |

What can go wrong without `flush()`
- Messages still in the outbox when the script exits are **lost**.
- Messages already shipped but with unread receipts are **safe**, but you never see the `ok`.

---

## 2. The code, line by line (labs/lab01_first_events/producer.py)

```python
COUNT = int(sys.argv[1]) if len(sys.argv) > 1 else 9   # producer.py 5000 sends 5000
USE_KEY = "--no-key" not in sys.argv                    # --no-key turns keys off

p = Producer({"bootstrap.servers": "localhost:9092"})   # where Kafka is; nothing sent yet

def done(err, msg):                                     # callback: once per receipt
    if err: print("FAILED", err)
    else:   print(f"ok key={msg.key()} partition={msg.partition()} offset={msg.offset()}")

order = {"order_id": i, "customer_id": f"C{i % 3}", "amount": 100 + i, "ts": time.time()}
p.produce(TOPIC, key=order["customer_id"] if USE_KEY else None,
          value=json.dumps(order), callback=done)       # queue it
p.poll(0)                                               # read receipts that arrived
p.flush()                                               # at the end: wait for the rest
```
- Key = customer ID, so one customer's orders share a partition.
- Value = the order as JSON text. Kafka only stores bytes and doesn't care what is inside.

---

## 3. Commands

```bash
cd /workspaces/streaming-lab
scripts/start.sh
docker exec kafka /opt/kafka/bin/kafka-topics.sh --bootstrap-server localhost:9092 --describe --topic orders   # expect PartitionCount: 3
docker exec kafka /opt/kafka/bin/kafka-get-offsets.sh --bootstrap-server localhost:9092 --topic orders         # end offsets per partition
grep -n "flush" labs/lab01_first_events/producer.py        # make sure p.flush() is NOT commented out

python labs/lab01_first_events/producer.py 9               # keyed
python labs/lab01_first_events/producer.py 9 --no-key      # no key
python labs/lab01_first_events/producer.py 5000 | grep -c "^ok"   # count receipts read

scripts/send.sh orders C9:a C9:b C9:c C9:d                 # per-key order test
scripts/console_consumer.sh                                # read; Ctrl+C to stop
```
If `PartitionCount` is 1:
```bash
docker exec kafka /opt/kafka/bin/kafka-topics.sh --bootstrap-server localhost:9092 --alter --topic orders --partitions 3
```

---

## 4. Experiments and what they showed

| # | Experiment | Result |
|---|---|---|
| 1 | Keyed run, twice | Each customer lands on the same partition both times |
| 2 | `--no-key` | `key=None`, messages spread across partitions in chunks |
| 3 | Kafka UI (port 8080) > Topics > orders > Messages | Offsets are consecutive per partition; key and JSON visible |
| 4 | `send.sh orders C9:a C9:b C9:c C9:d` | All four on one partition, in order a, b, c, d |
| 5 | Add `"city": "Mumbai"` to the event | New field shows in the message; Kafka doesn't care about contents |
| 6 | `flush()` commented out, 3 messages | Result depends on timing; can't be predicted |

Flush experiment with 5000 messages

| Run | "ok" lines | Offset before to after |
|---|---|---|
| `flush()` commented out | 4387 | 33 to 5033 |
| `flush()` enabled | 5000 | 5033 to 10033 |

All 5000 messages were stored both times. The script exited before reading about 613 receipts.

My partitions: C0 -> ___   C1 -> ___   C2 -> ___

---

## 5. Settings to know

| Setting | Plain meaning |
|---|---|
| `acks` | How many Kafka copies must confirm before you get a receipt (`all` is safest) |
| `linger.ms` | How long the courier waits to fill a batch (bigger = faster overall, small delay) |
| `enable.idempotence` | Stops retries from creating duplicates (Lab 3) |

---

## 6. Check-yourself answers (corrected)

1. What does `produce()` do? Queues the message in the outbox. It sends nothing and runs no callback.
2. Who runs `done`? It runs only when you call `poll()` or `flush()`, once per receipt that has arrived.
3. Why does a customer always land on the same partition? Same key, same partition, while the partition count is fixed.
4. What goes wrong without `flush()`? Outbox messages can be lost; unread receipts hide what succeeded.
5. Why 4387 "ok" lines but 5000 stored? Kafka sent every receipt; the script exited before reading about 613 of them.
6. Does an ack mean a consumer read the message? No. It means Kafka stored it.

---

## 7. Exit checklist
- [ ] I can explain outbox, courier and receipt in one minute
- [ ] I recorded the partition for each customer, stable across two runs
- [ ] I saw keyed vs unkeyed runs
- [ ] I can explain 4387 vs 5000

## 8. Problems seen this week
- Console producer needs `key:value` on every line; an empty line crashes it. Use `scripts/send.sh`.
- Topic had 1 partition; fixed with `--alter --partitions 3`.
- Run scripts from the repo root, not from `scripts/`.

## 9. My notes
- Producer flow in my own words:
- What `flush()` protects me from:
- One thing that surprised me:
