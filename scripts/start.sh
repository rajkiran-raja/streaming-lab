#!/usr/bin/env bash
set -e
docker compose up -d
echo "Waiting for Kafka to be healthy..."
until [ "$(docker inspect -f '{{.State.Health.Status}}' kafka 2>/dev/null)" = "healthy" ]; do
  sleep 3
done
echo "Kafka is ready. Kafka UI: open port 8080 in the Ports tab."
