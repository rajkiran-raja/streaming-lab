# Day 4: Python consumer

Goal: read from code and control where reading starts.

- group.id = team name; Kafka remembers each team's bookmark (committed offset)
- auto.offset.reset=earliest: a brand-new group starts from the first message
- Commit after processing: a crash then means a replay, not a lost message

## Steps
1. `python labs/lab01_first_events/consumer.py` and let it finish; stop and run again (nothing repeats).
2. New team: `python labs/lab01_first_events/consumer.py orders-app-2` (reads everything again).
3. Replay: `python labs/lab01_first_events/consumer.py orders-app --replay` (partition 0 from offset 2).

## Break it
Ctrl+C before the commit runs, restart, and see the message again (a duplicate).

## Check yourself
- Why commit after processing, not before?
- What is the difference between subscribe and assign?

## Notes
