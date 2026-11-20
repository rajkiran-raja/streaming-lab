# Day 2: Run Kafka on your machine

Goal: a working Kafka plus a web screen to look inside it.

## Steps
1. `scripts/start.sh` (starts Kafka and Kafka UI, waits until healthy)
2. `scripts/create_topic.sh orders 3`
3. Terminal A: `scripts/console_consumer.sh`
4. Terminal B: `scripts/console_producer.sh` then type lines like `C1:hello` and `C2:world`
5. Open Kafka UI on port 8080 -> Topics -> orders -> Messages. Note partition and offset.

## Break it
`docker compose restart kafka`, then run the console consumer again.
Your messages are still there because Kafka saves them to disk.

## Check yourself
- Which partition did C1 go to each time? Is it always the same?
- What does `--from-beginning` do?

## Notes
