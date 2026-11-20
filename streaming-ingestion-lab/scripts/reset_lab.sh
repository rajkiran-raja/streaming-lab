#!/usr/bin/env bash
# Deletes the orders topic and the orders-app group, then recreates the topic.
# Stop all consumers first.
docker exec kafka /opt/kafka/bin/kafka-consumer-groups.sh \
  --bootstrap-server localhost:9092 --delete --group orders-app 2>/dev/null || true
docker exec kafka /opt/kafka/bin/kafka-topics.sh \
  --bootstrap-server localhost:9092 --delete --topic orders 2>/dev/null || true
sleep 3
scripts/create_topic.sh orders 3
