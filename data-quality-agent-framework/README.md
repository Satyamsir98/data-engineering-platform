# ⚙️ Data Quality Agent Framework

## 📌 Overview

This project implements a configurable, multi-cloud data quality agent inspired by real-world data engineering pipelines.

It processes datasets dynamically, writes outputs to cloud storage (AWS S3 / Azure ADLS), and triggers downstream validation services via APIs.

---

## 🧠 Key Features

### 🔹 Config-Driven Execution

* Pipeline behavior controlled via YAML configuration
* No hardcoded endpoints or storage paths

### 🔹 Multi-Cloud Support

* Supports AWS S3 and Azure ADLS
* Dynamically switches based on configuration

### 🔹 Data Processing Simulation

* Processes datasets using dynamic definitions
* Mimics real-world Spark-based pipelines

### 🔹 API Integration

* Triggers downstream services after data processing
* Asynchronous API execution using threading

### 🔹 Job Status Tracking

* Tracks step-level execution status
* Simulates database updates for monitoring

---

## 🏗️ Architecture

```
Input Definitions → DQ Agent → Processing Layer → Cloud Storage → API Trigger → Status Tracking
```

---

## 📁 Project Structure

```
data-quality-agent-framework/
│
├── src/
│   ├── dq_agent.py
│   ├── utils/
│   │     ├── logger.py
│   │     ├── db.py
│   │     └── helpers.py
│   │
│   ├── connectors/
│   │     ├── aws_s3.py
│   │     └── azure_adls.py
│   │
│   └── services/
│         └── api_trigger.py
│
├── config/
│   └── config.yaml
│
├── tests/
│   └── test_dq_agent.py
│
├── main.py
├── requirements.txt
└── README.md
```

---

## ⚙️ How It Works

1. Load configuration from YAML
2. Read step definitions
3. Process each dataset dynamically
4. Write output to cloud storage
5. Trigger API for downstream validation
6. Update job execution status

---

## ▶️ Run the Project

```bash
python main.py
```

---

## 📊 Sample Execution Flow

```
Step 1 → Read dataset → Write to S3 → Trigger API → Update status  
Step 2 → Read dataset → Write to ADLS → Trigger API → Update status  
```

---

## ⚙️ Sample Config (`config.yaml`)

```yaml
cloud:
  default: aws

api:
  endpoint: http://mock-api/process
  timeout: 5
```

---

## 📊 Sample Definitions

```json
[
  {"step_name": "DQ Check 1", "df": "orders", "cloud": "aws"},
  {"step_name": "DQ Check 2", "df": "customers", "cloud": "azure"}
]
```

---

## 💡 Tech Stack

* Python
* PySpark (conceptual simulation)
* AWS S3 / Azure ADLS
* REST APIs

---

## 🎯 Use Cases

* Data quality validation pipelines
* Multi-cloud data processing workflows
* ETL/ELT validation layers
* Automated data checks and monitoring

---

## 💯 Highlights

* Config-driven architecture
* Multi-cloud support (AWS + Azure)
* Asynchronous API integration
* Modular and scalable design
* Testable pipeline with unit tests

---

## 👤 Author

Satyam Rai
Data Engineer | Agentic AI | PySpark | Data Platforms
