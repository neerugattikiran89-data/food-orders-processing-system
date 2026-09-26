import json
from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda value: json.dumps(value).encode("utf-8")
)

file_path = r"C:\Users\nbhar\OneDrive\Desktop\Food Delivery PipeLine\data\food_delivery_clean.json"

with open(file_path, "r", encoding="utf-8") as file:
    data = json.load(file)

print("Dataset loaded:", len(data))

for i, row in enumerate(data, start=1):
    producer.send("food_orders", value=row)

    if i % 1000 == 0:
        print("Records sent:", i)

producer.flush()

print("All records sent successfully!")

producer.close()