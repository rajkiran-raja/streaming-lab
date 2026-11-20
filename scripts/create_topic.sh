#!/usr/bin/env bash
# Usage: scripts/create_topic.sh [topic] [partitions]
TOPIC=${1:-orders}
PARTITIONS=${2:-3}
docker exec kafka /opt/kafka/bin/kafka-topics.sh \
  --bootstrap-server localhost:9092 \
  --create --if-not-exists \
  --topic "$TOPIC" --partitions "$PARTITIONS" --replication-factor 1
docker exec kafka /opt/kafka/bin/kafka-topics.sh \
  --bootstrap-server localhost:9092 --describe --topic "$TOPIC"
