from pyspark.sql import SparkSession

import os
os.environ["PYSPARK_PYTHON"] = r"D:\DLPYTHON\python.exe"      
os.environ["PYSPARK_DRIVER_PYTHON"] = r"D:\DLPYTHON\python.exe"  

spark = SparkSession.builder \
    .appName("TestSpark") \
    .master("local[*]") \
    .getOrCreate()

print("Spark session created successfully!")

df = spark.createDataFrame(
    [(1, "Alice"), (2, "Bob"), (3, "Charlie")],
    ["id", "name"]
)
df.show()

spark.stop()
