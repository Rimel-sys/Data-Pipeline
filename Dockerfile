FROM python:3

# Install project dependencies
RUN pip install -r requirements.txt

# Run project images
RUN docker-compose up -d
RUN docker-compose up

# Run kafka producer
CMD [ "python3", "producer.py" ]

# Run kafka consumer
CMD [ "python3", "consumer.py" ]

# Run spark streaming
start-master.sh
