import pandas as pd

def run_merge():
    df = pd.read_csv("data/silver_output.csv")

    result = df.groupby("user_id").size().reset_index(name="event_count")

    result.to_csv("data/gold_output.csv", index=False)

    print("[MERGE] Done")




# from utils.spark_session import get_spark
# import yaml
# from pyspark.sql.functions import count


# def run_merge():
#     spark = get_spark()

#     with open("config/config.yaml") as f:
#         config = yaml.safe_load(f)

#     silver_table = config["data"]["silver_table"]
#     gold_table = config["data"]["gold_table"]

#     # df = spark.table(silver_table)
#     df = spark.read.csv("data/silver_output", header=True, inferSchema=True)

#     agg_df = df.groupBy("user_id").agg(count("*").alias("event_count"))

#     agg_df.write.format("delta").mode("overwrite").saveAsTable(gold_table)

#     print(f"[MERGE] Aggregated data written to {gold_table}")


# if __name__ == "__main__":
#     run_merge()