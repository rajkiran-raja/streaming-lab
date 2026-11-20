# streaming-ingestion-lab

Hands-on labs to learn streaming data ingestion with Kafka, Python and (later) Spark and Delta.

## Run in GitHub Codespaces
1. Push this repo to GitHub.
2. Click Code -> Codespaces -> Create codespace on main.
3. Wait for the container to build (it installs Python packages and Docker-in-Docker).
4. In the terminal:
   ```bash
   scripts/start.sh
   scripts/create_topic.sh orders 3
   ```
5. Open the Ports tab and open port 8080 for Kafka UI.

## Run locally
Needs Docker and Python 3.9+.
```bash
pip install -r requirements.txt
scripts/start.sh
scripts/create_topic.sh orders 3
```

## Phase 1 plan (Week 1)
| Day | Topic | Where |
|---|---|---|
| 1 | Concepts | docs/day01_concepts.md |
| 2 | Run Kafka | docs/day02_run_kafka.md |
| 3 | Python producer | docs/day03_python_producer.md, labs/lab01_first_events |
| 4 | Python consumer | docs/day04_python_consumer.md, labs/lab01_first_events |
| 5 | Consumer groups and rebalancing | docs/day05_consumer_groups.md, labs/lab02_consumer_groups |
| 6 | Lag and consolidation | docs/day06_lag.md, labs/lab02_consumer_groups |
| 7 | Rebuild and test | docs/day07_test.md |

## Layout
- docker-compose.yml: Kafka (KRaft) + Kafka UI
- scripts/: start, stop, create topic, console producer/consumer, describe group (lag), reset lab
- labs/lab01_first_events/: Python producer and consumer
- labs/lab02_consumer_groups/: multi-worker consumer and bulk producer
- docs/: daily guides and your notes

## Useful commands
- Console producer (type `C1:hello`): `scripts/console_producer.sh`
- Console consumer: `scripts/console_consumer.sh`
- Lag: `scripts/describe_group.sh orders-app`
- Reset topic and group: `scripts/reset_lab.sh`
- Stop: `scripts/stop.sh`
