import os
import csv
import json
import uuid
from confluent_kafka import avro
from confluent_kafka.avro import AvroProducer
from kafka import KafkaProducer
from time import sleep
import pandas as pd

from properties import BROKER, TOPIC, APPNAME


def produce_data():
    producer = KafkaProducer(bootstrap_servers = BROKER, value_serializer=lambda v: json.dumps(v).encode('utf-8'))
    producer = KafkaProducer()

    if os.path.isfile('data_case_study.csv'):
        print("Data file already exists. \n Uploading data in progress...")
        try:
            data = pd.read_csv('data_case_study.csv', sep = ',')
            data['json'] = data.apply(lambda x: x.to_json(), axis=1)
            messages = data.json.tolist()
        except:
            print("Please check your CSV file data !")
    else:
        print("Data file does not exist !")
    for i in range(200):
        message_id = str(uuid.uuid4())
        message = {'request_id': message_id, 'data': json.loads(messages[i])}

        producer.send(topic=TOPIC, value=json.dumps(message).encode('utf-8'))
        producer.flush()

        print("\033[1;31;40m -- PRODUCER: Sent data with id {}".format(message_id))
        sleep(2)

if __name__ == '__main__':
    produce_data()
