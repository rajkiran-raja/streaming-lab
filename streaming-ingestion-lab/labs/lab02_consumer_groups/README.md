# Lab 2: Consumer groups, rebalancing and lag

## Day 5: rebalancing
Open 4 terminals plus one for the producer.
1. `python labs/lab02_consumer_groups/worker.py w1`
2. Start `w2`, then `w3`, then `w4` the same way. Watch ASSIGNED / REVOKED lines.
   With 3 partitions, the 4th worker gets nothing (idle).
3. `python labs/lab02_consumer_groups/bulk_producer.py 30` and see who prints which partition.
4. Ctrl+C one worker. The rest pick up its partition after a moment.
5. Compare strategies: restart workers with `--cooperative` and see fewer REVOKED lines.
6. Break it: `python labs/lab02_consumer_groups/worker.py slow1 --slow`
   The worker sleeps 15s without polling, so Kafka kicks it out (max.poll.interval.ms=10s).
7. Optional: simulate a crash with `kill -9 <pid>`. The group notices after session.timeout.ms (default 45s).

## Day 6: lag
1. Stop all workers.
2. `python labs/lab02_consumer_groups/bulk_producer.py 1000`
3. `scripts/describe_group.sh orders-app` and look at the LAG column (large).
4. Start one worker. Run describe_group again every few seconds and watch lag fall to 0.
5. Add a second and third worker and see lag fall faster.

## One-line takeaway (fill in)
-
