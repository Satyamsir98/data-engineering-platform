# 📄 Multi-Cloud PDF Extractor

## 📌 Overview

This project implements a document processing system that extracts structured data from files using a multi-cloud architecture.

The system dynamically routes processing between AWS-style and Azure-style pipelines based on configuration.

---

## 🧠 Key Features

### 🔹 Multi-Cloud Processing

* AWS-style document extraction flow
* Azure-style document analysis flow
* Config-driven execution

### 🔹 Table Extraction

* Converts document content into structured tabular format
* Outputs clean DataFrame and CSV

### 🔹 Dynamic Routing

* Automatically selects processing engine based on configuration

### 🔹 Modular Architecture

* Independent processing modules
* Easy to extend for additional providers

---

## 🏗️ Architecture

```
Input File → Cloud Selector → Processing Engine → Table Parser → Output CSV
```

---

## 📁 Project Structure

```
src/
 ├── pdf_extractor.py
 ├── aws_processor.py
 ├── azure_processor.py
 ├── parser.py
 └── utils.py

config/
 └── config.json

data/
 └── sample.txt

output/
 └── extracted.csv
```

---

## ⚙️ How It Works

1. Reads configuration (cloud type)
2. Loads input document
3. Routes to selected processing engine
4. Extracts tabular data
5. Saves output as CSV

---

## ▶️ Run the Project

```bash
python main.py
```

---

## 📊 Sample Output

```
    Item Price Qty
0  Apple    10   2
1 Banana     5   5
2   Milk    20   1
```

---

## 💡 Tech Stack

* Python
* Pandas

---

## 🎯 Use Cases

* Document data extraction
* Invoice parsing
* ETL preprocessing
* Structured data generation from text

---

## 💯 Highlights

* Multi-cloud architecture simulation
* Clean modular design
* Config-driven execution
* End-to-end data processing pipeline

---

## 👤 Author

Satyam Rai
Data Engineer | Multi-Cloud | Data Pipelines
