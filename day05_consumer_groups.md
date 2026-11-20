import json
import sys
import time

from confluent_kafka import Producer

TOPIC = "orders"
COUNT = int(sys.argv[1]) if len(sys.argv) > 1 else 9
USE_KEY = "--no-key" not in sys.argv

p = Producer({"bootstrap.servers": "localhost:9092"})


def done(err, msg):
    if err:
        print("FAILED", err)
    else:
        print(f"ok key={msg.key()} partition={msg.partition()} offset={msg.offset()}")


for i in range(1, COUNT + 1):
    order = {
        "order_id": i,
        "customer_id": f"C{i % 3}",
        "amount": 100 + i,
        "ts": time.time(),
    }
    p.produce(
        TOPIC,
        key=order["customer_id"] if USE_KEY else None,
        value=json.dumps(order),
        callback=done,
    )
    p.poll(0)

p.flush()
print("All messages delivered.")
