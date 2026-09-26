import json

file_path = r"C:\Users\nbhar\OneDrive\Desktop\Food Delivery PipeLine\India-Food-Delivery-Time-Prediction.txt"

print("Reading file...")

with open(file_path, "r", encoding="utf-8") as file:
    data = json.load(file)

print("File loaded successfully!")

print("Number of records:", len(data))

print("\nFirst record:")
print(data[0])

print("\nColumns:")
print(data[0].keys())