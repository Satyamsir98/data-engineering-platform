import pandas as pd

def run_transformation():
    df = pd.read_csv("data/bronze_output.csv")

    df = df.dropna(subset=["user_id"])

    df.to_csv("data/silver_output.csv", index=False)

    print("[TRANSFORMATION] Done")




# from utils.spark_session import get_spark
# import yaml
# from pyspark.sql.functions import col, to_timestamp


# def run_transformation():
#     spark = get_spark()

#     with open("config/config.yaml") as f:
#         config = yaml.safe_load(f)

#     bronze_table = config["data"]["bronze_table"]
#     silver_table = config["data"]["silver_table"]

#     # df = spark.table(bronze_table)
#     df = spark.read.csv("data/bronze_output", header=True, inferSchema=True)

#     transformed_df = df \
#         .withColumn("event_time", to_timestamp(col("event_time"))) \
#         .filter(col("user_id").isNotNull())

#     transformed_df.write.format("delta").mode("overwrite").saveAsTable(silver_table)

#     print(f"[TRANSFORMATION] Data written to {silver_table}")


# if __name__ == "__main__":
#     run_transformation()