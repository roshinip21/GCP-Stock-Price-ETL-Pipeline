# GCP Stock Market ETL Pipeline 🚀

This project implements a fully automated, production-grade ETL pipeline on Google Cloud Platform to ingest, transform, and store daily stock market data from a public API. The pipeline is built using Cloud Composer (Airflow), Cloud Functions, Cloud Storage, Dataflow (Apache Beam), and BigQuery.

---

## 📌 Project Overview

The goal is to automate the daily ingestion and processing of stock market data to create a reliable analytics backend. The raw data is extracted from a stock API, cleaned and enriched, and stored in BigQuery for downstream use.

---

## 🛠️ Tech Stack

- **Cloud Composer (Airflow)** – Orchestrates the daily ETL job  
- **Cloud Functions** – Event-driven trigger for Dataflow  
- **Cloud Storage** – Raw data landing zone  
- **Cloud Dataflow** – Cleansing, enrichment, and transformation  
- **BigQuery** – Final destination for structured, queryable data  
- **Python & Apache Beam** – For transformation logic  
- *(Optional)* Looker Studio – For visualization  

---

## 🧭 Architecture

<!-- Add your diagram image here -->
![Architecture Diagram](images/architecture-diagram.png)

**Flow Summary**:
1. **Cloud Composer** triggers a DAG daily to extract stock data via REST API and store it in **Cloud Storage**.
2. A **Cloud Function** listens for new files in the bucket and launches a **Dataflow** job.
3. The **Dataflow** pipeline reads, cleans, transforms, and loads the data into **BigQuery**.
4. *(Optional)* Visualizations can be built on top of BigQuery in **Looker Studio**.

---

## 📂 Project Structure


---


---

## ⚙️ Setup Instructions

1. **Enable GCP APIs**  
   - Cloud Composer, Functions, Dataflow, BigQuery, Storage

2. **Create Buckets & Datasets**  
   - Create a GCS bucket for raw data  
   - Create a BigQuery dataset (e.g., `stock_data`)

3. **Deploy Cloud Function**  


 ---

## 📈 Sample Outputs

<!-- Add screenshots or queries -->
![Sample BigQuery Table](images/sample-bq-table.png)

<!-- Optional dashboard -->
![Looker Dashboard](images/looker-dashboard.png)

---

## 📊 Sample KPIs & Metrics

- Daily Open/Close/Volume  
- Percentage Change and Moving Averages  
- Sector-wise Aggregates (if extended)  

---

## 📌 Future Improvements

- Add streaming support via Pub/Sub  
- Enrich data with news sentiment or technical indicators  
- Automate schema evolution in BigQuery  
- Add data validation and alerting (e.g., via Slack or Cloud Monitoring)

---

## 🤝 Credits

This project is inspired by [Data With Kunal's video](https://www.youtube.com/watch?v=gMbtyfgFW08) and extended with production-ready design practices.

---

## 📬 Contact

For suggestions or collaborations, feel free to reach out via [LinkedIn](https://www.linkedin.com/).

