from airflow.models import DAG
from airflow.utils.dates import days_ago
from airflow.operators.python import PythonOperator
from print_hello import print_hello
args ={
    "owner": "Faheem",
    "start_date": days_ago(1),
}

dag = DAG(
    dag_id ="Hello_World_DAG",
    default_args =args,
    schedule_interval='@daily'
)

with dag:
    hello_world =  PythonOperator(
        task_id ='hello_world',
        python_callable=print_hello
    )
    