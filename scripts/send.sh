#!/usr/bin/env bash
# Usage: scripts/send.sh orders C1:hello C2:world
TOPIC=$1; shift
printf '%s\n' "$@" | docker exec -i kafka /opt/kafka/bin/kafka-console-producer.sh \
  --bootstrap-server localhost:9092 --topic "$TOPIC" \
  --property parse.key=true --property key.separator=:
