# from airflow import DAG
# from airflow.operators.python import PythonOperator
# from datetime import datetime, timedelta

# from etl_01_klook_extract import etl_01_klook_extract


# default_args = {
#     "owner": "airflow",
#     "depends_on_past": False,
#     "email": ["your_email@example.com"],
#     "email_on_failure": False,
#     "email_on_retry": False,
#     "retries": 3,
#     "retry_delay": timedelta(minutes=5),
# }

# # 取得列表頁資料
# def run_klook_extract(**kwargs):
#     etl_01_klook_extract()




# with DAG(
#     dag_id="d_klook_etl",
#     default_args=default_args,
#     description="Klook etl",
#     schedule_interval="* * * * 2",
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
