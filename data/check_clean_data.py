import json

file_path = r"C:\Users\nbhar\OneDrive\Desktop\Food Delivery PipeLine\data\food_delivery_clean.json"

with open(file_path, "r", encoding="utf-8") as file:
    data = json.load(file)

print("Cleaned dataset loaded!")
print("Total records:", len(data))

print("\nFirst record:")
print(data[0])

print("\nWeather conditions:")
print(set(row["Weatherconditions"] for row in data))

print("\nRoad traffic density:")
print(set(row["Road_traffic_density"] for row in data))

print("\nCity:")
print(set(row["City"] for row in data))

print("\nDelivery time examples:")
for row in data[:5]:
    print(row["Time_taken(min)"])