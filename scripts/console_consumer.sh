#!/usr/bin/env bash
# Usage: scripts/console_consumer.sh [topic]
TOPIC=${1:-orders}
docker exec -it kafka /opt/kafka/bin/kafka-console-consumer.sh \
  --bootstrap-server localhost:9092 --topic "$TOPIC" --from-beginning \
  --property print.key=true --property print.partition=true --property print.offset=true
