from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import (
    StructType,
    StructField,
    StringType,
    DoubleType,
    IntegerType
)

spark = SparkSession.builder \
    .appName("FoodDeliveryParquet") \
    .getOrCreate()

spark.sparkContext.setLogLevel("WARN")

schema = StructType([
    StructField("ID", StringType(), True),
    StructField("Delivery_person_ID", StringType(), True),
    StructField("Delivery_person_Age", DoubleType(), True),
    StructField("Delivery_person_Ratings", DoubleType(), True),
    StructField("Restaurant_latitude", DoubleType(), True),
    StructField("Restaurant_longitude", DoubleType(), True),
    StructField("Delivery_location_latitude", DoubleType(), True),
    StructField("Delivery_location_longitude", DoubleType(), True),
    StructField("Order_Date", StringType(), True),
    StructField("Time_Orderd", StringType(), True),
    StructField("Time_Order_picked", StringType(), True),
    StructField("Weatherconditions", StringType(), True),
    StructField("Road_traffic_density", StringType(), True),
    StructField("Vehicle_condition", DoubleType(), True),
    StructField("Type_of_order", StringType(), True),
    StructField("Type_of_vehicle", StringType(), True),
    StructField("multiple_deliveries", DoubleType(), True),
    StructField("Festival", StringType(), True),
    StructField("City", StringType(), True),
    StructField("Time_taken(min)", IntegerType(), True)
])

kafka_df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "kafka:29092") \
    .option("subscribe", "food_orders") \
    .option("startingOffsets", "earliest") \
    .load()

json_df = kafka_df.select(
    col("value").cast("string").alias("json_data")
)

food_df = json_df.select(
    from_json(col("json_data"), schema).alias("data")
).select("data.*")

query = food_df.writeStream \
    .format("parquet") \
    .outputMode("append") \
    .option("path", "/opt/parquet") \
    .option("checkpointLocation", "/opt/checkpoint") \
    .trigger(availableNow=True) \
    .start()

query.awaitTermination()