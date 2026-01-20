from notebooks.ingestion import run_ingestion
from notebooks.transformation import run_transformation
from notebooks.delta_merge import run_merge


if __name__ == "__main__":
    print("Starting Databricks Delta Pipeline...")

    run_ingestion()
    run_transformation()
    run_merge()

    print("Pipeline completed successfully!")