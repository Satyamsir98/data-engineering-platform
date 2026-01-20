# ⚙️ Databricks Delta Live Pipeline (Simulated)

## 📌 Overview

This project implements a Databricks-style Delta Lake pipeline using a Medallion Architecture approach (Bronze → Silver → Gold).

It demonstrates how raw data is ingested, transformed, and aggregated into analytics-ready datasets.
For local execution, the pipeline is simulated using Pandas while maintaining the same architectural design used in Databricks.

---

## 🧠 Key Features

### 🔹 Medallion Architecture

* Bronze → Raw data ingestion
* Silver → Cleaned and validated data
* Gold → Aggregated business metrics

### 🔹 Delta Lake Inspired Design

* Incremental-ready pipeline structure
* Separation of storage layers
* Scalable transformation approach

### 🔹 Config-Driven Pipeline

* Input paths and table names managed via configuration
* Flexible and reusable design

### 🔹 Local Simulation with Pandas

* Uses Pandas for local execution
* Mimics PySpark/Databricks transformations

### 🔹 Modular Notebooks Structure

* Separate modules for ingestion, transformation, and aggregation
* Clean and maintainable code

---

## 🏗️ Architecture

```
Raw Data → Bronze Layer → Silver Layer → Gold Layer → Analytics Output
```

---

## 📁 Project Structure

```
databricks-delta-live-pipeline/
│
├── notebooks/
│   ├── ingestion.py
│   ├── transformation.py
│   └── delta_merge.py
│
├── data/
│   ├── user_activity.csv
│   ├── bronze_output.csv
│   ├── silver_output.csv
│   └── gold_output.csv
│
├── config/
│   └── config.yaml
│
├── utils/
│   └── spark_session.py
│
├── main.py
├── requirements.txt
└── README.md
```

---

## ⚙️ How It Works

1. Load input dataset
2. Ingest raw data into Bronze layer
3. Clean and validate data in Silver layer
4. Aggregate user-level metrics in Gold layer
5. Store final output for analytics

---

## ▶️ Run the Project

```
python main.py
```

---

## 📊 Sample Input

```
user_id,event_time
1,2024-01-01 10:00:00
2,2024-01-01 11:00:00
1,2024-01-02 09:00:00
3,2024-01-02 12:00:00
```

---

## 📊 Sample Output (Gold Layer)

```
user_id,event_count
1,2
2,1
3,1
```

---

## 💡 Tech Stack

* Python
* Pandas (for local simulation)
* PySpark (conceptual / real environment)
* Delta Lake concepts

---

## 🎯 Use Cases

* User activity analytics
* Event tracking pipelines
* Incremental data processing systems
* Data warehouse preparation

---

## 💯 Highlights

* Implements Medallion Architecture
* Simulates Delta Lake pipeline locally
* Clean modular design
* Production-inspired structure
* Easy to extend for real Databricks environment

---

## 🧠 Note

This project simulates a Databricks Delta pipeline locally using Pandas due to environment constraints.
In real-world scenarios, PySpark and Delta Lake would be used for scalable distributed processing.

---

## 👤 Author

Satyam Rai
Data Engineer | PySpark | Data Platforms | Databricks
