# ⚙️ Microsoft Fabric Medallion Data Pipeline (Simulated)

## 📌 Overview

This project implements a Microsoft Fabric-style Medallion Architecture pipeline (Bronze → Silver → Gold) for processing and analyzing sales data.

It demonstrates how raw data is ingested, cleaned, and transformed into business-ready aggregated insights.
The pipeline is designed to simulate Microsoft Fabric's Lakehouse architecture using local execution.

---

## 🧠 Key Features

### 🔹 Medallion Architecture

* Bronze → Raw data ingestion
* Silver → Cleaned and validated data
* Gold → Aggregated business metrics

### 🔹 Fabric-Inspired Design

* Simulates OneLake and Lakehouse concepts
* Layered data processing architecture
* Structured pipeline execution

### 🔹 Config-Driven Pipeline

* Input and output paths controlled via YAML
* Easily configurable and reusable

### 🔹 Modular Processing

* Separate modules for each layer
* Clean and maintainable structure

### 🔹 Local Simulation

* Uses Pandas for local execution
* Mimics real Fabric data pipelines

---

## 🏗️ Architecture

```
Raw Data → Bronze Layer → Silver Layer → Gold Layer → Analytics Output
```

---

## 📁 Project Structure

```
fabric-medallion-data-pipeline/
│
├── notebooks/
│   ├── bronze_ingestion.py
│   ├── silver_transformation.py
│   └── gold_aggregation.py
│
├── data/
│   └── raw_sales_data.csv
│
├── output/
│   ├── bronze/
│   │     └── bronze_sales.csv
│   ├── silver/
│   │     └── silver_sales.csv
│   └── gold/
│         └── gold_sales_metrics.csv
│
├── config/
│   └── config.yaml
│
├── pipeline/
│   └── orchestration_flow.md
│
├── utils/
│   ├── logger.py
│   └── helpers.py
│
├── main.py
├── requirements.txt
└── README.md
```

---

## ⚙️ How It Works

1. Load raw sales data
2. Ingest into Bronze layer
3. Clean and validate in Silver layer
4. Aggregate metrics in Gold layer
5. Store outputs for analytics

---

## ▶️ Run the Project

```
python main.py
```

---

## 📊 Sample Input

```
product,amount,date
A,100,2024-01-01
B,200,2024-01-02
A,150,2024-01-03
C,300,2024-01-04
B,250,2024-01-05
```

---

## 📊 Sample Output (Gold Layer)

```
product,total_sales
A,250
B,450
C,300
```

---

## 💡 Tech Stack

* Python
* Pandas (for local simulation)
* Microsoft Fabric concepts (Lakehouse, OneLake)

---

## 🎯 Use Cases

* Sales analytics pipelines
* Data warehouse preparation
* Data transformation workflows
* Business reporting pipelines

---

## 💯 Highlights

* Implements Medallion Architecture
* Simulates Microsoft Fabric pipeline
* Config-driven and modular design
* Production-style structure
* Easy to extend to real Fabric environment

---

## 🧠 Note

This project simulates a Microsoft Fabric pipeline locally using Pandas.
In real-world implementations, Fabric Lakehouse, Dataflows, and Spark notebooks would be used for scalable processing.

---

## 👤 Author

Satyam Rai
Data Engineer | Microsoft Fabric | PySpark | Data Platforms
