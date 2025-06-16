# import sys
# import os
# from datetime import datetime
# from airflow import DAG
# from airflow.operators.python import PythonOperator

# # ✅ 動態加入 src 路徑 (Docker 裡面)
# CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))  # /opt/airflow/dags
# SRC_DIR = os.path.abspath(os.path.join(CURRENT_DIR, '../src'))  # /opt/airflow/src

# print(f'>>> Docker src 路徑: {SRC_DIR}')

# if SRC_DIR not in sys.path:
#     sys.path.insert(0, SRC_DIR)
#     print(f'>>> sys.path 已加入: {SRC_DIR}')

# # ✅ 匯入 src/accupass 裡的程式
# from accupass import t_accupass_data_clean

# # ✅ 定義要跑的 function
# def run_data_clean():
#     t_accupass_data_clean.main()

# # ✅ 定義 DAG
# with DAG(
#     dag_id='d_02_accupass_clean',
#     schedule_interval=None,
#     # start_date=datetime(2025, 5, 12),
#     catchup=False,
# ) as dag:

#     task_clean_data = PythonOperator(
#         task_id='run_data_clean',
#         python_callable=run_data_clean,
#     )
