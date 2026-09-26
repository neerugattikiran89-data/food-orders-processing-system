import json

input_file = r"C:\Users\nbhar\OneDrive\Desktop\Food Delivery PipeLine\India-Food-Delivery-Time-Prediction.txt"

output_file = r"C:\Users\nbhar\OneDrive\Desktop\Food Delivery PipeLine\data\food_delivery_clean.json"


with open(input_file, "r", encoding="utf-8") as file:
    data = json.load(file)

print("Dataset loaded:", len(data))


for row in data:
    for column in row:
        if isinstance(row[column], str):
            row[column] = row[column].strip()


for row in data:
    for column in row:
        if row[column] == "NaN":
            row[column] = None


for row in data:
    if row["Weatherconditions"] is not None:

        row["Weatherconditions"] = row["Weatherconditions"].replace(
            "conditions ", ""
        )

        if row["Weatherconditions"] == "NaN":
            row["Weatherconditions"] = None



for row in data:
    row["Time_taken(min)"] = int(
        row["Time_taken(min)"].replace("(min) ", "")
    )


numeric_columns = [
    "Delivery_person_Age",
    "Delivery_person_Ratings",
    "Restaurant_latitude",
    "Restaurant_longitude",
    "Delivery_location_latitude",
    "Delivery_location_longitude",
    "Vehicle_condition",
    "multiple_deliveries"
]

for row in data:
    for column in numeric_columns:
        if row[column] is not None:
            row[column] = float(row[column])



with open(output_file, "w", encoding="utf-8") as file:
    json.dump(data, file, indent=2)

print("Cleaning completed!")
print("Cleaned file saved successfully.")