#!/usr/bin/env bash
# Usage: scripts/console_producer.sh [topic]
# Type key:value lines, e.g.  C1:hello
TOPIC=${1:-orders}
docker exec -it kafka /opt/kafka/bin/kafka-console-producer.sh \
  --bootstrap-server localhost:9092 --topic "$TOPIC" \
  --property parse.key=true --property key.separator=:
