# Day 6: Lag and consolidation

Goal: learn the one number that shows pipeline health.

lag = latest offset on the partition - your committed offset
- Near 0: keeping up. Growing: consumers are slow, stuck or dead.

## Steps
Follow labs/lab02_consumer_groups/README.md, "Day 6".

## Write your takeaways
- Lab 1: Ordering is only guaranteed within a partition, so the key choice is a design decision.
- Lab 2: Parallelism is capped by partition count, and consumers beyond it sit idle.
(Rewrite them in your own words.)

## Teach it
Explain Days 1 to 5 aloud for 5 minutes as if to a junior engineer. Where you get stuck is what to re-read.

## Notes
