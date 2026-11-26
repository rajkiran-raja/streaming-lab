import json
import sys

from confluent_kafka import Consumer, TopicPartition

TOPIC = "orders"
GROUP = sys.argv[1] if len(sys.argv) > 1 and not sys.argv[1].startswith("--") else "orders-app"

c = Consumer(
    {
        "bootstrap.servers": "localhost:9092",
        "group.id": GROUP, # The team name. Different names mean different bookmarks.
        "auto.offset.reset": "earliest", # Where a team with no bookmark starts: at offset 0.
        "enable.auto.commit": False, # We save the bookmark ourselves, after processing, instead of letting Kafka save it on a timer.
    }
)

if "--replay" in sys.argv:
    c.assign([TopicPartition(TOPIC, 0, 2)])
else:
    c.subscribe([TOPIC]) # Join the team. Kafka gives you partitions and tracks the team’s bookmark.
    # subscribe vs assign. subscribe joins a team and uses its bookmark. assign picks an exact partition and offset yourself, with no team, no rebalancing and no bookmark. --replay uses assign.
print(f"Reading '{TOPIC}' as group '{GROUP}'. Ctrl+C to stop.")
try:
    while True:
        m = c.poll(1.0) # Wait up to 1 second for a message. It returns None when nothing is new.
        if m is None:
            continue
        if m.error():
            print(m.error())
            continue
        raw = m.value().decode("utf-8", errors="replace") # Kafka gives bytes. We turn them into text, then try JSON, and fall back to showing plain text.
        try:
            value = json.loads(raw)
        except json.JSONDecodeError:
            value = f"(not JSON) {raw}"
        print(m.partition(), m.offset(), m.key(), value)
        if "--replay" not in sys.argv:
            c.commit(message=m) # Saves the bookmark just after this message, and only after we printed it. That is the safe order.
except KeyboardInterrupt:
    pass
finally:
    c.close()
