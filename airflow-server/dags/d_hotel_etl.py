# from airflow import DAG
# from airflow.operators.python import PythonOperator
# from datetime import datetime, timedelta

# from hotel.accomo01_extract_get_opensource import 
# from hotel.accomo02_transform_filter import 
# from hotel.accomo03_extract_booking import 
# from hotel.accomo04_clean import 
# from hotel.accomo05_match import 
# from hotel.accomo06_export_sql import 
# from hotel.accomo08_update_rating import 
# from hotel.accomo09_delete_import import 


# default_args = {
#     "owner": "airflow",
#     "depends_on_past": False,
#     "email": ["your_email@example.com"],
#     "email_on_failure": False,
#     "email_on_retry": False,
#     "retries": 3,
#     "retry_delay": timedelta(minutes=5),
# }

# def run_accupass_crawler(**kwargs):
#     e_accupass_crawler()

# def run_accupass_data_clean(**kwargs):
#     t_accupass_data_clean()

# def run_accupuass_mysql(**kwargs):
#     l_accupass_mysql_con()

# with DAG(
#     dag_id="d_accupass_etl",
#     default_args=default_args,
#     description="Accupass etl",
#     schedule_interval="* * * * 5,
#     catchup=False,
#     tags=["crawler", "clean", "to_mySQL"]
# ) as dag:

#     task1 = PythonOperator(
#         task_id="accupass_crawler",
#         python_callable=run_accupass_crawler,
#     )

#     task2 = PythonOperator(
#         task_id="accupass_clean",
#         python_callable=run_accupass_data_clean,
#     )

#     task3 = PythonOperator(
#         task_id="accupass_to_SQL",
#         python_callable=run_accupuass_mysql,
#     )

#     task1 >> task2 >> task3
