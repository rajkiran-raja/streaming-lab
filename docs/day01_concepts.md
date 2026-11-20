# Day 1: Kafka concepts (no code)

- Topic: one notebook (e.g. orders)
- Partition: one page of the notebook; order is guaranteed only inside one partition
- Offset: line number on a page; starts at 0, per partition
- Broker: server that stores the notebooks
- Producer / Consumer: writes / reads
- Consumer group: team of readers; each partition goes to one reader in the team
- KRaft: Kafka manages itself, no ZooKeeper needed
- Lag: latest offset minus your committed offset

## Do
1. Read the list twice.
2. Draw from memory: Producer -> Topic (3 partitions) -> Consumer group.
3. Say aloud: "Order is guaranteed only inside one partition."

## Recall questions
1. What does offset 5 on partition 2 mean? (the 6th message on partition 2)
2. Why does the key matter?
3. Why do consumers beyond the partition count sit idle?

## My answers
