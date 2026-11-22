import json
import sys

from confluent_kafka import Consumer, TopicPartition

TOPIC = "orders"
GROUP = sys.argv[1] if len(sys.argv) > 1 and not sys.argv[1].startswith("--") else "orders-app"

c = Consumer(
    {
        "bootstrap.servers": "localhost:9092",
        "group.id": GROUP,
        "auto.offset.reset": "earliest",
        "enable.auto.commit": False,
    }
)

if "--replay" in sys.argv:
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
        raw = m.value().decode("utf-8", errors="replace")
        try:
            value = json.loads(raw)
        except json.JSONDecodeError:
            value = f"(not JSON) {raw}"
        print(m.partition(), m.offset(), m.key(), value)
        if "--replay" not in sys.argv:
            c.commit(message=m)
except KeyboardInterrupt:
    pass
finally:
    c.close()