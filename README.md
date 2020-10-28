Case Study Version_3
This project is a Machine Learning Pipeline intended to help data engineers quickly stream data and predict it using a Spark/Kafka infrastructure.

Overview
## Components
Zookeeper
https://zookeeper.apache.org/
An open source server for distributed coordination.
Kafka
https://kafka.apache.org/
Open source distributed streaming platform
Users of this project will interact with Kafka in several ways:
Writing to Kafka using a simple producer program written in Python
Reading from Kafka using a simple consumer program written in Python
Reading from Kafka using Apache Spark
Kafka data is not persisted outside of the image, so each restart of the container will result in a new data set
## Spark
https://spark.apache.org/
Spark Streaming is an extension of the core Spark API that enables scalable, high-throughput, fault-tolerant stream processing of live data streams.
## Hbase (Optional)
https://hbase.apache.org/
Apache HBase™ is the Hadoop database, a distributed, scalable, big data store.
## Project Structure
docker-compose - Docker compose service definitions
producer.py - Basic producer which sends test data to Kafka
consumer.py - Basic consumer to quickly validate that data is flowing to Kafka
stream.py - Basic Spark Streaming to stream data from kafka and apply modification
predictor.py - Basic ML script to predict the activity types for each timestamp using the pretrained model
Dockerfile - Basic commands to run the project
properties.py - Environment variables of the project
Description.txt - Description of the case_study_v3
data_case_study.csv - Basic file of the data used
requirements.txt - Python package requirements
Getting Started
## Prerequisites
docker-compose
Python (Tested with 3.6; should be compatible with 2.7)
