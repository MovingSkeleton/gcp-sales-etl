from airflow import DAG
from datetime import datetime
from airflow.providers.google.cloud.transfers.gcs_to_bigquery import GCSToBigQueryOperator

#Config
PROJECT_ID="single-scholar-482212-q3"
BUCKET_NAME="etl-composer-files"
DATASET_ID="data_staging"
TABLE_ID="sample_Table2"

default_args={
    "owner":"sqlinminutes@gmail.com",
    "start_date":datetime(2026,1,1)
}

with DAG(
    dag_id="sampleCSVMigrationDAG",
    default_args=default_args,
    schedule_interval="@once",
    catchup=False,
)as dag:

    CsvToBq=GCSToBigQueryOperator(
        task_id="CsvToBq",
        source_format="CSV",
        bucket=BUCKET_NAME,
        source_objects="customer.csv",
        destination_project_dataset_table="single-scholar-482212-q3.data_staging.sample_Table2",
        skip_leading_rows=1,
        write_disposition="WRITE_TRUNCATE",
        autodetect=True,

    )
    CsvToBq
