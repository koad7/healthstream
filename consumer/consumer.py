#!/usr/bin/env python
from confluent_kafka import Consumer, KafkaException
import sys

conf = {
    'bootstrap.servers': 'kafka-1:19092',  # Kafka broker address
    'group.id': 'hello_group',
    'auto.offset.reset': 'earliest',
}

def main():
    consumer = Consumer(conf)

    def print_assignment(consumer, partitions):
        print('Assignment:', partitions)

    consumer.subscribe(['hello_topic'], on_assign=print_assignment)

    try:
        while True:
            msg = consumer.poll(timeout=1.0)
            if msg is None:
                continue
            if msg.error():
                if msg.error().code() == KafkaException._PARTITION_EOF:
                    sys.stderr.write('%% %s [%d] reached end at offset %d\n' %
                                     (msg.topic(), msg.partition(), msg.offset()))
                elif msg.error():
                    raise KafkaException(msg.error())
            else:
                print('Received message: {}'.format(msg.value().decode('utf-8')))

    finally:
        # Close down consumer to commit final offsets.
        consumer.close()

if __name__ == '__main__':
    main()
