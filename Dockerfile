FROM apache/airflow:3.3.2-python3.11

COPY --chown=airflow:root requirements.txt /opt/airflow/requirements.txt

RUN pip install --no-cache-dir --requirement /opt/airflow/requirements.txt
