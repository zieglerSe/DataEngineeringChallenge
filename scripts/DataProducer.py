import pandas as pd 
import time 
import json 
import random 
from kafka import KafkaProducer

def serializer(message):
    return json.dumps(message).encode('utf-8')

# Kafka Producer
producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=serializer
)

file_path = "sample_data.csv"

df = pd.read_csv(file_path)
df = df.rename(columns={
    "Unknown": "partition",
    "$schema": "schema"
})


if __name__ == '__main__':
    for i in range(0, (len(df))):
        # get row i of df
        row = df.iloc[i]
        # Convert the row to a dictionary
        row_dict = row.to_dict()
        # Convert the row to a JSON string
        messages = pd.DataFrame.to_json(row)

        print(json.dumps(messages, indent=4))
        print(i)

        if row_dict["wiki"] == "dewiki":
            producer.send('editsAll', messages)
            producer.send('editsGermany', messages)
        else:
            producer.send('editsAll', messages)

        # Sleep for a random number of seconds between 0 and 1
        time_to_sleep = random.random()
        time.sleep(time_to_sleep)


