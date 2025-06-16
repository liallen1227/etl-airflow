# from airflow import DAG
# from airflow.operators.python import PythonOperator
# from datetime import datetime, timedelta

# from food.food01_extract_get_opensource import food01_extract_get_opensource
# from food.food02_transform_filter import food02_transform_filter
# from food.food03_extract_googleapi_text_search import food03_extract_googleapi_text_search
# from food.food04_compare_name_and_add import food04_compare_name_and_add


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
#     dag_id="d_food_etl",
#     default_args=default_args,
#     description="food etl",
#     schedule_interval="* * * * 3",
#     catchup=False,
#     tags=["crawler", "clean", "to_mySQL"]
# ) as dag:

#     task1 = PythonOperator(
#         task_id="get_open_data",
#         python_callable=food01_extract_get_opensource,
#     )

#     task2 = PythonOperator(
#         task_id="drop_open_data_noneed",
#         python_callable=food02_transform_filter
#     )

#     task3 = PythonOperator(
#         task_id="get_googleapi_data",
#         python_callable=food03_extract_googleapi_text_search,
#     )

#     task4 = PythonOperator(
#         task_id="compare_opensource_and_googleapi_data",
#         python_callable=food04_compare_name_and_add,
#     )

#     task1 >> task2 >> task3 >> task4
