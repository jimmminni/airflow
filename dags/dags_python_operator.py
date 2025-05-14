from airflow import DAG
import pendulum
import datetime
from airflow.operators.python import PythonOperator

with DAG(
    dag_id="dags_python_operator",
    schedule="30 6 * * *",
    start_date=pendulum.datetime(2023, 3, 1, tz="Asia/Seoul"),
    catchup=False
) as dag:
    def select_fruit():
        fuit = ['APPLE', 'BANANA', 'ORANGE', 'AVOCADO']
        rand_int = random.randint(0, 3)
        print(fruit[rand_int])