# Day 5: Consumer groups and rebalancing

Goal: understand how a team of readers shares pages.

- 3 partitions + 1 consumer: it gets all 3
- 3 partitions + 3 consumers: one each
- 3 partitions + 4 consumers: the 4th is idle
- Rebalance = Kafka re-dealing partitions when a consumer joins, leaves or dies
- Eager: everyone drops everything and is re-dealt (brief pause)
- Cooperative-sticky: only the partitions that must move are moved

## Steps
Follow labs/lab02_consumer_groups/README.md, "Day 5".

## Break it
Run `worker.py slow1 --slow` and watch Kafka kick the consumer out for not polling in time.

## Check yourself
- What triggers a rebalance?
- Why does partition count cap parallelism?

## Notes
