from notebooks.bronze_ingestion import run_bronze
from notebooks.silver_transformation import run_silver
from notebooks.gold_aggregation import run_gold


if __name__ == "__main__":
    print("Starting Fabric Medallion Pipeline...\n")

    run_bronze()
    run_silver()
    run_gold()

    print("\nPipeline completed successfully!")