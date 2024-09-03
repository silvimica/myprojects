from airflow.models import DAG
from airflow.providers.postgres.operators.postgres import PostgresOperator
from airflow.operators.python import PythonOperator
from airflow.models.connection import Connection
from datetime import datetime
from airflow.models.baseoperator import chain
from data_migration.data_migration_2 import *

tables_from='{{tables_from}}'.replace(' ', '').split(',')
tables_to='{{tables_to}}'.replace(' ', '').split(',')

fun_args = {
            'from_': '{{ from_ }}', 
            'to_': '{{ to_ }}', 
            'conn_from': '{{ conn_from }}',
            'conn_to': '{{ conn_to }}', 
            'table_from': '',
            'table_to': '',
            'schema_from':'{{schema_from }}',
            'schema_to':'{{ schema_to }}',
            'truncate': '{{ truncate_table }}'
            }

default_args = {'owner' : "{{ owner }}"}
schedule = "@{{ schedule }}"
start_date = datetime.strptime("{{ start_date }}", '%Y-%m-%d %H:%M:%S')
task_list=[]

with DAG("{{ dag_id }}", start_date=start_date, catchup=False, schedule_interval = schedule, default_args=default_args) as dag:

    for table_from,table_to in zip(tables_from, tables_to):
        fun_args['table_from']=table_from
        fun_args['table_to']=table_to
        migrate = PythonOperator(task_id=f'{table_from}_{table_to}', python_callable=data_migration, op_kwargs=fun_args,trigger_rule='all_done')
        task_list.append(migrate)

chain(*task_list)
