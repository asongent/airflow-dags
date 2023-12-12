from airflow.contrib.operators.spark_submit_operator import SparkSubmitOperator

spark_task = SparkSubmitOperator(
    task_id='spark_task',
    conn_id='spark',
    application='/kubernetes/job.py',
    verbose=False,
    conf={'key': 'value'},
    application_args=['arg1', 'arg2'],
    dag=dag,
)
