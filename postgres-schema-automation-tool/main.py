import json
from src.config_loader import load_config
from src.extractor import extract_schema
from src.deployer import deploy_schema
from src.validator import validate_schema
from src.utils import log


def main():
    config = load_config()

    tables = config["tables"]
    target_schema = config["target_schema"]

    log("Step 1: Extract")
    ddl_data = extract_schema(tables)

    with open("output/ddl_output.json", "w") as f:
        json.dump(ddl_data, f, indent=4)

    log("Step 2: Deploy")
    deploy_schema(ddl_data, target_schema)

    log("Step 3: Validate")
    report = validate_schema(tables)

    with open("output/validation_report.json", "w") as f:
        json.dump(report, f, indent=4)

    log("Done")


if __name__ == "__main__":
    main()