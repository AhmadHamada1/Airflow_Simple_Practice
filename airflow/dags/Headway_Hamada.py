from datetime import timedelta, datetime

from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago

from airflow import DAG

# Default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': True,
    'start_date': datetime.now()- timedelta(days=2),  
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False
}

# Define the DAG
dag = DAG(
    'Headway_Hamada',
    default_args=default_args,
    description='prints messages',
    schedule_interval='@hourly',
)

# Task to print "Headway Giza Systems"
print_headway = PythonOperator(
    task_id='print_headway',
    python_callable=lambda: print("Headway Giza Systems"),
    dag=dag,
)

# Task to print "SRE track"
print_sre = PythonOperator(
    task_id='print_sre',
    python_callable=lambda: print("SRE track"),
    dag=dag,
)

# Define task dependencies (print_headway runs first, then print_sre)
print_headway >> print_sre
