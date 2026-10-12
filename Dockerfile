FROM apache/airflow:slim-3.3.2-python3.11

RUN pip install --no-cache-dir --upgrade \
    apache-airflow-providers-standard==1.20.0 \
    asyncpg==0.31.0 \
    psycopg2-binary==2.9.10 \
    python-dotenv==1.2.4 \
    pyjwt==2.15.1 \
    setuptools==83.0.0 \
    urllib3==2.8.0 \
    uv==0.12.18
