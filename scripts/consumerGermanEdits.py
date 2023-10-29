from kafka import KafkaConsumer
from kafka import KafkaProducer
import json 
import time

def serializer(message):
    return json.dumps(message).encode('utf-8')

# Kafka consumer configuration
consumer = KafkaConsumer(
    'editsGermany',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest'
)

producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=serializer
)

relative_path = "outputGermany.txt"

# Initialize variables to track message count and time
message_count = 0
start_time = time.time()

try:
    for message in consumer:
        # Message received, record the timestamp and increase the count
        message_count += 1
        current_time = time.time()

        # Calculate the average messages per minute every minute
        if current_time - start_time >= 60:
            messages_per_minute = message_count
            producer.send('avgGermany', messages_per_minute)
            with open(relative_path, 'a') as file:
                # Convert the value to a string and write it to the file 
                file.write((str(current_time)) + " average messages per minute " + (str(messages_per_minute)) + ',')
                file.write('\n')
            print(f"Average messages per minute: {messages_per_minute}")
            message_count = 0
            start_time = current_time

except KeyboardInterrupt:
    pass
finally:
    consumer.close()
