import requests
import csv
from google.cloud import storage
from datetime import datetime


today = datetime.today().strftime('%Y-%m-%d')
url = f'https://api.upstox.com/v2/historical-candle/NSE_EQ%7CINE848E01016/month/{today}'

headers = {
        "Accept": "application/json"  # Replace with your RapidAPI key
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json().get('data', []).get('candles', [])  # Extracting the 'rank' data
    csv_filename = 'tradingData.csv'
    print(data)
    if data:
        # Write data to CSV file with only specified field names
        with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            for entry in data:
                writer.writerow(entry)

        print(f"Data fetched successfully and written to '{csv_filename}'")

        # Reading and printing first five rows
        # with open(csv_filename, mode='r') as file:
        #     reader = csv.reader(file)
        #     for i, row in enumerate(reader):
        #         print(row)
        #         if i == 4:  # Stop after five rows
        #             break


        #Upload the CSV file to GCS
        bucket_name = 'etl_source_bucket'
        storage_client = storage.Client()
        bucket = storage_client.bucket(bucket_name)
        destination_blob_name = f'{csv_filename}'  # The path to store in GCS

        blob = bucket.blob(destination_blob_name)
        blob.upload_from_filename(csv_filename)

        print(f"File {csv_filename} uploaded to GCS bucket {bucket_name} as {destination_blob_name}")
    else:
        print("No data available from the API.")
else:
    print("Failed to fetch data:", response.status_code)
