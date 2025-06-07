# 📊 Stock Market ETL Pipeline on GCP

This project implements a batch ETL (Extract, Transform, Load) pipeline using Google Cloud services including Cloud Composer (Apache Airflow), Cloud Storage, Cloud Functions, Dataflow, and BigQuery. The pipeline automates the ingestion of daily stock trading data, applies transformations, and loads it into BigQuery for analytics.

---

## 🧩 Architecture Overview

<!-- Add architecture diagram image here -->

**Workflow Summary:**
1. **Cloud Composer (Airflow)** triggers a DAG daily to fetch stock trading data via a public API.
2. The data is saved as a CSV in **Google Cloud Storage**.
3. A **Cloud Function** listens for new files and triggers a **Dataflow** job.
4. The **Dataflow** pipeline cleans, transforms, and enriches the data using UDFs and schema metadata.
5. Processed data is written into a **BigQuery** table for downstream analysis.

---

## 📁 Project Structure

```
GCP-Stock-Price-ETL-Pipeline/
├── dag.py
├── fetch_data.py
├── metaData/
│   ├── bq.json
│   └── udf.js
├── cloud run function/
│   ├── main.py
│   └── requirments.txt
├── tradingData.csv
└── README.md
```

---

## ⚙️ Technologies Used

- **Apache Airflow / Cloud Composer** – DAG scheduling and orchestration
- **Cloud Storage (GCS)** – File-based data ingestion and storage
- **Cloud Functions** – Serverless trigger to launch Dataflow
- **Cloud Dataflow (Apache Beam)** – Data transformation and processing
- **BigQuery** – Scalable data warehousing and analytics

---

## 🚀 How the Pipeline Works

<!-- Add a workflow or flowchart image here -->


1. **Scheduled Extraction**  
   A Cloud Composer DAG triggers a Python script (`fetch_data.py`) to fetch daily stock data from a public API and upload it to a GCS bucket.

2. **Event-driven Trigger**  
   A Cloud Function listens for new file uploads in GCS. When triggered, it reads metadata and launches a Dataflow job.

3. **Dataflow Processing**  
   The Dataflow job uses the `udf.js` and `bq.json` to transform raw CSV data, clean null values, and enrich with calculated fields (e.g., % change, moving averages).

4. **BigQuery Loading**  
   The final output is written to a BigQuery table in an analytics-ready format, supporting queries and dashboards.



## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/ETL-pipeline-Batch-processing-with-Airflow.git
cd ETL-pipeline-Batch-processing-with-Airflow
````

### 2. Configure GCP Environment

* Create a **GCS bucket** for staging data
* Create a **BigQuery dataset** and configure schema using `metaData/bq.json`
* Enable required APIs: Composer, Cloud Functions, Dataflow, BigQuery, Cloud Storage

### 3. Deploy Cloud Function

```bash
gcloud functions deploy trigger_dataflow \
  --runtime python311 \
  --trigger-resource <your-bucket-name> \
  --trigger-event google.storage.object.finalize \
  --entry-point main \
  --source ./cloud\ run\ function \
  --region <your-region>
```

### 4. Set Up Composer DAG

* Upload `dag.py` to your Cloud Composer DAGs folder
* Configure Airflow variables and GCP connections as needed

### 5. Run the Pipeline

* Upload a new `tradingData.csv` to GCS to simulate a new data pull
* Watch the Cloud Function and Dataflow job logs
* Verify the processed data in your BigQuery table

---

## 📈 Sample Output and Visualization

<!-- Add image of sample data or query results -->


Created dashboards using Looker Studio, Data Studio BI Tool connected to BigQuery.

---

## ✅ Best Practices Followed

* Event-driven architecture using GCS and Cloud Functions
* Modular pipeline with clear separation of extraction, transformation, and loading
* Reusable metadata and schema definitions
* Serverless and autoscaling components

---

## 🔒 IAM & Permissions Checklist

* Cloud Function SA → Needs `Dataflow Developer` and `Storage Object Viewer`
* Composer SA → Needs permission to trigger GCS uploads and run DAG tasks
* BigQuery → Grant write access to Dataflow job and read access to analytics tools


---

## 📬 Contact

For questions, contributions, or feedback, please open an issue or reach out via [LinkedIn]((https://www.linkedin.com/in/roshini-p21/)).
