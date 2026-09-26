import os
from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("FoodDeliveryParquetToMySQL") \
    .getOrCreate()

spark.sparkContext.setLogLevel("WARN")

df = spark.read.parquet("/opt/parquet")

print("Records read from Parquet:", df.count())

mysql_host = "172.31.186.224"
mysql_port = "3306"
database = "food_delivery"

jdbc_url = f"jdbc:mysql://{mysql_host}:{mysql_port}/{database}"



properties = {
    "user": os.getenv("MYSQL_USER", "food_pipeline"),
    "password": os.getenv("MYSQL_PASSWORD"),
    "driver": "com.mysql.cj.jdbc.Driver"
}

df.write \
    .option("batchsize", "5000") \
    .option("numPartitions", "1") \
    .jdbc(
        url=jdbc_url,
        table="food_orders",
        mode="append",
        properties=properties
    )

print("All data successfully loaded into MySQL!")

spark.stop()