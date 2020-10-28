from kafka import KafkaConsumer
import json

from properties import BROKER, TOPIC, APPNAME


def consume_data():
    consumer = KafkaConsumer(TOPIC, bootstrap_servers=BROKER)
    for msg in consumer:
        message = json.loads(msg.value)
        print('\033[1;32;40m ** CONSUMER: Received data for request id {}'.format(message['request_id']))

if __name__ == '__main__':
    consume_data()
