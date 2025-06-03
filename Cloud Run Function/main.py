import functions_framework
from googleapiclient.discovery import build
import json
from google.auth import default
from google.cloud import storage

@functions_framework.cloud_event
def hello_gcs(cloud_event):
    # Extract metadata from the event
    data = cloud_event.data
    event_id = cloud_event["id"]
    event_type = cloud_event["type"]

    bucket_name = data["bucket"]
    file_name = data["name"]
    metageneration = data.get("metageneration")
    time_created = data.get("timeCreated")
    updated = data.get("updated")

    region = "us-south1"
    project = "etl-project-461623"
    template_path = "gs://dataflow-templates-us-south1/latest/GCS_Text_to_BigQuery"

    print(f"Event ID: {event_id}")
    print(f"Event type: {event_type}")
    print(f"Bucket: {bucket_name}")
    print(f"File: {file_name}")
    print(f"Metageneration: {metageneration}")
    print(f"Created: {time_created}")
    print(f"Updated: {updated}")

    # Prevent re-processing moved files
    if file_name.startswith("etl_source_bucket/"):
        print(f"File {file_name} is already processed. Skipping Dataflow job.")
        return

    try:
        # Authenticate and build Dataflow service
        credentials, _ = default()
        dataflow = build('dataflow', 'v1b3', credentials=credentials)

        # Set Dataflow job parameters
        template_body = {
            "jobName": f"cf-bq-load-{event_id[:8]}",
            "parameters": {
                "javascriptTextTransformGcsPath": "gs://trading-dataflow-metadata/udf.js",
                "JSONPath": "gs://trading-dataflow-metadata/bq.json",
                "javascriptTextTransformFunctionName": "transform",
                "outputTable": "etl-project-461623.dev1_gcs_sink.dev1-df-cf-trading-data",
                "inputFilePattern": f"gs://{bucket_name}/{file_name}",
                "bigQueryLoadingTemporaryDirectory": "gs://trading-dataflow-metadata",
            }
        }

        print(f"Launching Dataflow with body:\n{json.dumps(template_body, indent=2)}")

        response = dataflow.projects().locations().templates().launch(
            projectId=project,
            location=region,
            gcsPath=template_path,
            body=template_body
        ).execute()

        print(f"Dataflow job launched successfully:\n{json.dumps(response, indent=2)}")

    except Exception as e:
        print(f"Error: {str(e)}")

