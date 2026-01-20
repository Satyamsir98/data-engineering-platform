import pandas as pd
import yaml

def run_ingestion():
    with open("config/config.yaml") as f:
        config = yaml.safe_load(f)

    input_path = config["data"]["input_path"]

    df = pd.read_csv(input_path)

    df.to_csv("data/bronze_output.csv", index=False)

    print("[INGESTION] Done")




# from utils.spark_session import get_spark
# import yaml


# def run_ingestion():
#     spark = get_spark()

#     with open("config/config.yaml") as f:
#         config = yaml.safe_load(f)

#     input_path = config["data"]["input_path"]
#     bronze_table = config["data"]["bronze_table"]

#     df = spark.read.csv(input_path, header=True, inferSchema=True)

#     df.write.mode("overwrite").csv("data/bronze_output", header=True)
#     # df.write.format("delta").mode("overwrite").saveAsTable(bronze_table)

#     print(f"[INGESTION] Loaded data into {bronze_table}")


# if __name__ == "__main__":
#     run_ingestion()