from airflow import dags
from airflow.utils.dates import days_ago
from airflow.operators.empty import EmptyOperator

default_args={
    "owner":"Movingskeleton"
}

with DAG(
    dag_id= 'sales_etl_pipeline'
    start_date=days_ago(1),
    schedule_interval="@daily",
    catchup=False,
    tags=['sales','etl'],
    default_args=default_args,

) as dag:
    
    start=EmptyOperator(
        task_id='start'
    )

    end=EmptyOperator(
        task_id='end'
    )
    start>>end