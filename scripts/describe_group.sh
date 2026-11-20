#!/usr/bin/env bash
# Usage: scripts/describe_group.sh [group]
GROUP=${1:-orders-app}
docker exec kafka /opt/kafka/bin/kafka-consumer-groups.sh \
  --bootstrap-server localhost:9092 --describe --group "$GROUP"
