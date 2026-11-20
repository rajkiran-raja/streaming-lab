import json
import sys
import time

from confluent_kafka import Producer

TOPIC = "orders"
COUNT = int(sys.argv[1]) if len(sys.argv) > 1 else 1000

p = Producer({"bootstrap.servers": "localhost:9092"})
for i in range(1, COUNT + 1):
    order = {"order_id": i, "customer_id": f"C{i % 3}", "amount": 100 + i, "ts": time.time()}
    p.produce(TOPIC, key=order["customer_id"], value=json.dumps(order))
    if i % 500 == 0:
        p.poll(0)
p.flush()
print(f"Sent {COUNT} messages to '{TOPIC}'.")
