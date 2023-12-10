FROM apache/airflow:2.7.3
RUN pip install pyspark
RUN pip install apache-airflow-providers-apache-spark
COPY requirements.txt /

RUN pip install --no-cache-dir "apache-airflow==${AIRFLOW_VERSION}" -r /requirements.txt