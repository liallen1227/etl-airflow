# from airflow import DAG
# from airflow.operators.python import PythonOperator
# from airflow.sensors.external_task import ExternalTaskSensor
# from datetime import datetime, timedelta

# from food.food05_extract_google_info import food05_extract_google_info
# from food.food06_clean_openhours_name import food06_clean_openhours_name
# from food.food07_load_mysql import food07_load_mysql


# default_args = {
#     "owner": "airflow",
#     "depends_on_past": False,
#     "email": ["your_email@example.com"],
#     "email_on_failure": False,
#     "email_on_retry": False,
#     "retries": 3,
#     "retry_delay": timedelta(minutes=5),
# }

# with DAG(
#     dag_id="d_food_update_etl",
#     default_args=default_args,
#     description="food update etl",
#     schedule_interval="* * * * *",
#     catchup=False,
#     tags=["checkdata", "crawler", "clean", "to_mySQL"]
# ) as dag:

#     wait_for_food_etl = ExternalTaskSensor(
#         task_id="wait_for_food_etl",
#         external_dag_id="d_food_etl",
#         external_task_id=None, # 不指定 task_id 代表等整個 DAG 完成
#         mode="poke",
#         timeout=600, # 最多等 10 分鐘
#         poke_interval=30, # 每 30 秒檢查一次對方 DAG 狀態
#         retries=2,
#     )

#     task5 = PythonOperator(
#         task_id="get_google_data",
#         python_callable=food05_extract_google_info,
#     )

#     task6 = PythonOperator(
#         task_id="clean_data",
#         python_callable=food06_clean_openhours_name,
#     )

#     task7 = PythonOperator(
#         task_id="load_mysql",
#         python_callable=food07_load_mysql,
#     )

#     wait_for_food_etl >> task5 >> task6 >> task7
