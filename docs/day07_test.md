# Day 7: Rebuild and test

1. `scripts/stop.sh`, then delete the topic with `scripts/reset_lab.sh` (or start fresh).
2. Rebuild Labs 1 and 2 from scratch in under 30 minutes without notes.
3. Answer aloud, then check below.

## Questions
1. Why do keys matter?
2. What triggers a rebalance?
3. What does lag tell you?
4. Why is a 4th consumer idle on 3 partitions?
5. Why commit after processing?

## Answers
1. Same key -> same partition, so per-key order is kept.
2. A consumer joins, leaves, crashes, or misses its poll deadline.
3. How far consumers are behind the writers; whether they keep up.
4. A partition goes to only one consumer in a group.
5. A crash before the commit means a replay, not a lost message.

## Exit checklist
- [ ] Explain partition vs consumer group in 30 seconds
- [ ] Predict which partition a keyed message goes to
- [ ] Read lag and name what makes it grow
- [ ] Explain the tradeoff of committing before vs after processing
