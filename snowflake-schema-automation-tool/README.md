
# 🚀 Schema Sync Tool (Snowflake)

## 📌 Overview

This project provides an end-to-end schema automation solution that extracts, deploys, and validates database schemas across environments.

It supports:

* Snowflake

The system is designed to simulate real-world data platform workflows using modular, production-style architecture.

---

## 🧠 Key Features

### 🔹 Schema Extraction

* Extracts table DDL dynamically
* Supports multiple tables
* Handles column definitions and constraints

### 🔹 Schema Deployment

* Executes DDL statements on target systems
* Handles schema qualification
* Supports environment-based deployment

### 🔹 Schema Validation

* Table existence validation
* Column-level comparison
* Primary key validation
* Foreign key validation

### 🔹 Modular Architecture

* Clean separation of concerns
* Plug-and-play components
* Easily extendable for other databases

---

## 🏗️ Architecture

```
Extract → Transform (DDL Clean) → Deploy → Validate
```

Components:

* Extractor
* DDL Processor
* Deployer
* Validator
* Config-driven execution

---

## 📁 Project Structure

```
src/
 ├── extractor.py
 ├── deployer.py
 ├── validator.py
 ├── ddl_processor.py
 ├── snowflake_client.py
 ├── config_loader.py
 └── utils.py

config/
 └── config.json

output/
 ├── ddl_output.json
 └── validation_report.json

main.py
```

---

## ⚙️ How It Works

1. Load configuration (tables, schemas)
2. Extract DDL from source
3. Process and clean DDL
4. Deploy schema to target
5. Validate schema consistency

---

## ▶️ Run the Project

```bash
python main.py
```

---

## 📊 Sample Output

### DDL Output

```json
[
    {
        "table": "customers",
    "ddl": "CREATE TABLE customers (id INT, name TEXT);"
  }
]
```

### Validation Report

```json
[
    ["customers", "Table Exists", "Success"],
  ["customers", "Column Compare", "Success"]
]
```

---

## 🧪 Note

This project uses **mocked database connections** for demonstration purposes.

To run with real databases:

* Provide valid Snowflake credentials
* Replace mock client logic with actual connectors

---

## 💡 Tech Stack

* Python
* Snowflake Connector (optional)
* JSON-based config

---

## 🎯 Use Cases

* Schema migration
* Environment sync (Dev → Prod)
* Data platform automation
* ETL validation pipelines

---

## 💯 Highlights

* End-to-end automation (Extract → Deploy → Validate)
* Multi-database support
* Production-style modular design
* Resume-ready real-world system

---

## 👤 Author

Satyam Rai
Data Engineer | PySpark | AWS | Azure | Data Platforms



    <!-- # Snowflake Schema Automation/Sync Tool
    
    ## Overview
    End-to-end schema automation tool for Snowflake.
    
    ## Features
    - Extract table DDL
    - Deploy schema to target
    - Validate schema (columns, PK, FK)
    
    ## Run
    python main.py -->