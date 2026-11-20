import json
import sys

from confluent_kafka import Consumer, TopicPartition

TOPIC = "orders"
GROUP = sys.argv[1] if len(sys.argv) > 1 else "orders-app"

c = Consumer(
    {
        "bootstrap.servers": "localhost:9092",
        "group.id": GROUP,
        "auto.offset.reset": "earliest",
        "enable.auto.commit": False,
    }
)

if "--replay" in sys.argv:
    # Replay: read partition 0 from offset 2 without using group balancing
    c.assign([TopicPartition(TOPIC, 0, 2)])
else:
    c.subscribe([TOPIC])

print(f"Reading '{TOPIC}' as group '{GROUP}'. Ctrl+C to stop.")
try:
    while True:
        m = c.poll(1.0)
        if m is None:
            continue
        if m.error():
            print(m.error())
            continue
        print(m.partition(), m.offset(), m.key(), json.loads(m.value()))
        if "--replay" not in sys.argv:
            c.commit(message=m)
except KeyboardInterrupt:
    pass
finally:
    c.close()
