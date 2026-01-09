from airflow import DAG
from airflow.operators.dummy import DummyOperator
from airflow.operators.python import PythonOperator
from datetime import datetime

default_args = {
    "owner": "ani",
    "retries": 2,
}

def push_sum(**context):
    a, b = 10, 20
    total=a+b
    context['ti'].xcom_push(key='total_sum',value=total)
    print(f"Push sum : {total}")

def pull_sum(**context):
    total=context['ti'].xcom_pull(
        task_id="push_sum_task",
        key="total sum"
    )
    print("Pulled sum={total} from XCom")

with DAG(
    dag_id="dummy_Xcom_DAG",
    schedule_interval="@once",
    start_date=datetime(2025, 1, 1),
    default_args=default_args,
    catchup=False,
) as dag:

    start = DummyOperator(
        task_id="startTask"
    )

    push_sum_task = PythonOperator(
        task_id="PushSumTask",
        python_callable=push_sum,
        provide_context=True,
    )

    pull_sum_task=PythonOperator(
        task_id="pullSumTask",
        python_callable=pull_sum,
        provide_context=True,
    )
    close = DummyOperator(
        task_id="endTask"
    )

    start >> getsum_task >> close
