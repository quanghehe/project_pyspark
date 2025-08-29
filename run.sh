docker exec -it spark-master spark-submit --master spark://spark-master:7077 --packages org.postgresql:postgresql:42.6.0 /opt/spark/data/load_json.py
