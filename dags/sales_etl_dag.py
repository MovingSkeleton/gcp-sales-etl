from airflow import dags
from airflow.utils.dates import days_ago
from airflow.operators.empty import EmptyOperator

with DAG(
    dag_id= 'sales_etl_pipeline'
    start_date=days_ago(1),
    schedule_interval="@daily",
    catchup=False,
    tags=['sales','etl'],

) as dag:
    
    start=EmptyOperator(
        task_id='start'
    )

    end=EmptyOperator(
        task_id='end'
    )
    start>>end