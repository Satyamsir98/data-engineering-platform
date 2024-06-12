# ⚙️ Dynamic Data Transformation Engine

## 📌 Overview

This project implements a dynamic, config-driven data transformation engine inspired by real-world ETL frameworks.

It allows users to define transformations declaratively via configuration, which are then applied dynamically to datasets.

---

## 🧠 Key Features

### 🔹 Dynamic Transformation Execution

* Applies transformations based on configuration
* No hardcoded logic in pipeline

### 🔹 Transformation Registry

* Central registry for transformation classes
* Easily extendable with new transformations

### 🔹 Multiple Transformation Types

* String transformations (upper, lower, trim)
* Mathematical transformations (round, abs, mod)
* Date transformations (date conversion, comparison)
* Regex-based transformations and more

### 🔹 Modular Design

* Each transformation is an independent class
* Clean separation of logic

---

## 🏗️ Architecture

```
Input Data → Transformation Engine → Registry → Transformation Classes → Output Data
```

---

## 📁 Project Structure

```
src/
 ├── engine.py
 ├── registry.py
 ├── transformations/
 │     ├── base.py
 │     ├── string_transforms.py
 │     ├── math_transforms.py
 │     └── date_transforms.py
 └── utils.py

config/
 └── config.json

data/
 └── sample.csv

output/
 └── result.csv
```

---

## ⚙️ How It Works

1. Load input dataset
2. Read transformation config
3. Loop through transformations
4. Dynamically apply each transformation
5. Save transformed dataset

---

## ▶️ Run the Project

```bash
python main.py
```

---

## 📊 Sample Input

```
name,amount,date
john,100.5,2024-01-01
alice,200.3,2024-02-01
```

---

## 📊 Sample Config

```json
[
  {
    "type": "upper",
    "columns": ["name"]
  },
  {
    "type": "round",
    "columns": ["amount"],
    "params": 1
  }
]
```

---

## 📊 Sample Output

```
name_upper,amount_round
JOHN,100.5
ALICE,200.3
```

---

## 💡 Tech Stack

* Python
* Pandas

---

## 🎯 Use Cases

* ETL pipelines
* Data standardization
* Data preprocessing
* Config-driven data workflows

---

## 💯 Highlights

* Implements transformation registry pattern
* Supports scalable transformation addition
* Production-style architecture
* Config-driven execution

---

## 👤 Author

Satyam Rai
Data Engineer | PySpark | Data Platforms
