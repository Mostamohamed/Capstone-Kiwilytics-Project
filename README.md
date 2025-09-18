# 🚀 Total Revenue per Day ETL with Airflow

## Overview
This project demonstrates an **end-to-end automated ETL pipeline** built with **Apache Airflow**.  
It extracts sales data from a **PostgreSQL database**, transforms it using **Python (pandas)**, and calculates **total revenue per day**.  
The pipeline also generates a **time series visualization** of revenue trends, making it a strong portfolio project for **data engineering and analytics workflows**.

---

## ✨ Features
- **Extract**: Query order and product data from PostgreSQL  
- **Transform**: Clean, join, and aggregate revenue with pandas (`groupby` on order_date)  
- **Load**: Save results as CSV and PNG outputs for analysis  
- **Schedule**: Automated daily execution with Apache Airflow  
- **Visualize**: Generate daily revenue plots for clear trend analysis  

---

## 📂 Project Structure
```
total_revenue_pipeline/
│
├── dags/                      
│   └── sales_revenue_dag.py    # Main Airflow DAG
├── data/
│   └── RetailDB_postgres.sql   # Sample database schema
├── outputs/
│   ├── daily_sales_data.csv    # Processed sales data
│   ├── daily_revenue.csv       # Aggregated daily revenue
│   └── daily_revenue_plot.png  # Visualization of revenue trends
└── README.md                   
```

---

## ⚙️ Pipeline Workflow
The Airflow DAG (`sales_revenue_pipeline`) includes three main tasks:

1. **Extract Data** – Pulls daily sales data by joining `orders`, `order_details`, and `products`.  
2. **Transform Data** – Calculates total and average revenue per day.  
3. **Load & Visualize** – Saves results into CSV files and generates a line plot of daily revenue.  

---

## 🛠 Tools & Technologies
- **Apache Airflow** – Workflow orchestration  
- **PostgreSQL** – Source database  
- **Python (pandas, matplotlib)** – Data transformation & visualization  

---

## ▶️ How to Run
1. Configure your Airflow environment and add a Postgres connection (`postgres_conn`).  
2. Place the DAG file inside the `dags/` directory.  
3. Start Airflow and trigger the `sales_revenue_pipeline` DAG.  
4. Check the `outputs/` folder (or `/tmp/`) for generated CSVs and revenue plots.  

---

## 📊 Example Visualization
<img width="600" src="https://github.com/user-attachments/assets/9d67e65f-d6d1-490e-890a-0889901afd4b" />

---

✅ **Outcome**: Automated daily extraction, computation, and visualization of sales revenue → delivering **clear insights** into revenue trends and supporting **data-driven decisions**.  

