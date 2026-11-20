# Day 3: Python producer

Goal: send order events from code and understand keys.

- Key = label on the message (customer id). Same key -> same partition -> per-key order kept.
- `produce()` only queues the message; `poll(0)` serves delivery callbacks; `flush()` waits until all are delivered.

## Steps
1. `python labs/lab01_first_events/producer.py` (keyed)
2. Check the printed partition for each customer.
3. `python labs/lab01_first_events/producer.py 9 --no-key`
4. Compare partitions with the keyed run.

## Break it
Run with `--no-key` and see one customer's orders scatter across partitions.

## Check yourself
- What happens if you forget `flush()` and the script exits?
- Why is the key choice a design decision?

## Notes
