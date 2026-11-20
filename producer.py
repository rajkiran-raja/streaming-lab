import json
import os
import sys
import time

from confluent_kafka import Consumer

TOPIC = "orders"
GROUP = "orders-app"
name = sys.argv[1] if len(sys.argv) > 1 and not sys.argv[1].startswith("--") else f"worker-{os.getpid()}"
COOP = "--cooperative" in sys.argv
SLOW = "--slow" in sys.argv

conf = {
    "bootstrap.servers": "localhost:9092",
    "group.id": GROUP,
    "client.id": name,
    "auto.offset.reset": "earliest",
    "enable.auto.commit": False,
}
if COOP:
    conf["partition.assignment.strategy"] = "cooperative-sticky"
if SLOW:
    conf["max.poll.interval.ms"] = 10000

c = Consumer(conf)


def on_assign(consumer, partitions):
    print(f"[{name}] ASSIGNED:", sorted(p.partition for p in partitions), flush=True)


def on_revoke(consumer, partitions):
    print(f"[{name}] REVOKED: ", sorted(p.partition for p in partitions), flush=True)


c.subscribe([TOPIC], on_assign=on_assign, on_revoke=on_revoke)
print(f"[{name}] started (cooperative={COOP}, slow={SLOW}). Ctrl+C to stop.", flush=True)

first = True
try:
    while True:
        m = c.poll(1.0)
        if m is None:
            continue
        if m.error():
            print(f"[{name}] error:", m.error(), flush=True)
            continue
        order = json.loads(m.value())
        print(f"[{name}] p{m.partition()} off{m.offset()} key={m.key()} order={order['order_id']}", flush=True)
        c.commit(message=m)
        if SLOW and first:
            first = False
            print(f"[{name}] sleeping 15s without polling (max.poll.interval.ms=10s)...", flush=True)
            time.sleep(15)
except KeyboardInterrupt:
    pass
finally:
    c.close()
