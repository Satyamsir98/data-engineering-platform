# 🌩️ Cloud-Agnostic ETL Pipeline (Airflow + Spark)

## 📌 Overview

This project demonstrates a cloud-agnostic ETL pipeline built using Apache Airflow and Python, capable of processing data across AWS and Azure environments through a configurable abstraction layer.

---

## 🧠 Key Features

### 🔹 ETL Pipeline

* Extract → Transform → Load workflow
* Modular components for each stage

### 🔹 Airflow Orchestration

* DAG-based execution
* Task scheduling and monitoring

### 🔹 Cloud-Agnostic Design

* Supports AWS (S3) and Azure (ADLS)
* Config-driven cloud selection

### 🔹 Data Transformation

* Null handling
* Data filtering
* Column enrichment

---

## 🏗️ Architecture

```id="etl1"
Data Source → Extract → Transform → Load → Target Storage
                ↓
            Airflow DAG
```

Components:

* Airflow DAG
* Extract Module
* Transform Module
* Load Module
* Cloud I/O Layer

---

## 📁 Project Structure

```id="etl2"
dags/
 └── etl_pipeline.py

src/
 ├── extract.py
 ├── transform.py
 ├── load.py
 ├── cloud_io.py
 └── utils.py

config/
 └── config.json

data/
 ├── sample.csv
 └── output.csv
```

---

## ⚙️ How It Works

1. Read input data from source (local / S3 / ADLS)
2. Apply transformations (cleaning, filtering)
3. Write processed data to target
4. Managed via Airflow DAG

---

## ▶️ Run the Project

### Local Test

```bash id="etl3"
python test_run.py
```

### Airflow

* Start Airflow scheduler & webserver
* Trigger DAG: `cloud_agnostic_etl`

---

## 📊 Sample Output

```text id="etl4"
Data loaded: 6 rows
Transformed data: 4 rows
Data written to output.csv
```

---

## 🧪 Sample Data

* Includes null values and invalid records
* Demonstrates data cleaning and validation

---

## 💡 Tech Stack

* Apache Airflow
* Python (Pandas / PySpark style logic)
* AWS / Azure (simulated)

---

## 🎯 Use Cases

* Data ingestion pipelines
* Multi-cloud data processing
* Batch ETL workflows
* Data engineering pipelines

---

## 💯 Highlights

* Multi-cloud support (AWS + Azure)
* Config-driven pipeline design
* Production-style modular architecture
* Airflow-based orchestration

---

## 👤 Author

Satyam Rai
Data Engineer | ETL Pipelines | Cloud Data Platforms
