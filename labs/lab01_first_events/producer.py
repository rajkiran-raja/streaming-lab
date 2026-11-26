import json
import sys
import time

from confluent_kafka import Producer

TOPIC = "orders"
COUNT = int(sys.argv[1]) if len(sys.argv) > 1 else 9 #arg passed wih the script to send msgs
USE_KEY = "--no-key" not in sys.argv

p = Producer({
    "bootstrap.servers": "localhost:9092",
    "linger.ms": 100,
}) # Creates the producer and tells it where Kafka is


def done(err, msg):
    if err:
        print("FAILED", err)
    else:
        print(f"ok key={msg.key()} partition={msg.partition()} offset={msg.offset()}") # msg.partition() and msg.offset() tell you where Kafka stored the message.


for i in range(1, COUNT + 1):
    order = { # Builds the event.
        "order_id": i,
        "customer_id": f"C{i % 3}",
        "city": "Mumbai",
        "amount": 100 + i,
        "ts": time.time(),
    }
    p.produce( # Queues the message
        TOPIC,
        key=order["customer_id"] if USE_KEY else None,
        value=json.dumps(order),
        callback=done,
    )
    p.poll(0) # reads any receipts that have arrived

p.flush() # at the end waits for the rest of receits
print("All messages delivered.")
