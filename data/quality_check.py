import json
from collections import Counter

file_path = r"C:\Users\nbhar\OneDrive\Desktop\Food Delivery PipeLine\India-Food-Delivery-Time-Prediction.txt"

print("Reading dataset...")

with open(file_path, "r", encoding="utf-8") as file:
    data = json.load(file)

print("Dataset loaded successfully!")
print("Total records:", len(data))

print("\n Missing Values")

for column in data[0]:
    values = [row[column] for row in data]
    missing = sum(
        value is None or str(value).strip().lower() == "nan"
        for value in values
    )
    print(column, ":", missing)

    print("\n===== DUPLICATE IDs =====")

ids = [row["ID"].strip() for row in data]
counts = Counter(ids)

duplicates = [id for id, count in counts.items() if count > 1]

print("Duplicate IDs:", len(duplicates))


print("\n===== UNIQUE VALUES =====")

for column in [
    "Weatherconditions",
    "Road_traffic_density",
    "Vehicle_condition",
    "Type_of_order",
    "Type_of_vehicle",
    "multiple_deliveries",
    "Festival",
    "City"
]:
    values = set(str(row[column]).strip() for row in data)
    print(column, ":", values)


print("\nQuality check completed!")

      