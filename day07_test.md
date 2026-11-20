# Lab 1: First events

Goal: send events from Python, read them back, and see partitions, keys and offsets.

## Steps
1. Start Kafka: `scripts/start.sh`
2. Create the topic: `scripts/create_topic.sh orders 3`
3. Terminal A: `python labs/lab01_first_events/consumer.py`
4. Terminal B: `python labs/lab01_first_events/producer.py`
5. Open Kafka UI (port 8080) -> Topics -> orders -> Messages.

## Experiments
- Run the producer with `--no-key` and compare partitions with the keyed run.
- Run the consumer with a new group name: `python labs/lab01_first_events/consumer.py orders-app-2` and see it re-read everything.
- Replay from a chosen offset: `python labs/lab01_first_events/consumer.py orders-app --replay`
- Stop the consumer with Ctrl+C before it commits and see the message again on restart.

## One-line takeaway (fill in)
-
