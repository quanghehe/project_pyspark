from pyspark.sql import SparkSession
from pyspark.sql.functions import to_json, struct

spark = SparkSession.builder \
    .appName("Load JSON to Postgres") \
    .master("spark://spark-master:7077") \
    .getOrCreate()

df = spark.read.json("/opt/spark/data/nocibe.json",multiLine=True)
raw_df = df.select(to_json(struct("*")).alias("raw_json"))

# Config Postgres
db_url = "jdbc:postgresql://postgres:5432/product"
db_properties = {
    "user": "quang",
    "password": "q",
    "driver": "org.postgresql.Driver"
}


raw_df.write.jdbc(
    url=db_url, table="nocibe_raw", mode="overwrite", properties=db_properties
)

print("JSON data loaded into Postgres!")
spark.stop()
