# from airflow import DAG
# from airflow.operators.python import PythonOperator
# from datetime import datetime, timedelta

# from spot.spot01_extract_get_opensource import 
# from spot.spot02_transform_filter import 
# from spot.spot03_extract_googleapi_text_search import 
# from spot.spot04_compare_name_and_add import 
# from spot.spot05_extract_google_info import 
# from spot.spot06_clean_openhours_name import 
# from spot.spot07_load_mysql import 


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
#     schedule_interval="* * * * 4",
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
