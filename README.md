# FDA NDC ETL Pipeline

## Overview

This project collects drug information from the [FDA NDC (National Drug Code) Directory API](https://open.fda.gov/apis/drug/ndc/) and processes it through an ETL (Extract, Transform, Load) pipeline to store the data in a PostgreSQL database.

## Requirements
- Python 3.10+
- PostgreSQL
- Apache Airflow
- Dependencies outlined in `requirements.txt`

## Installation
```bash
pip install -r requirements.txt
```
## Project Structure
- `notebooks/`: Jupyter notebooks for testing and development
- `src/`: Source code for the ETL pipeline
  - `extract.py`: Script for extracting data from the FDA NDC API
  - `transform.py`: Script for transforming the extracted data
  - `load.py`: Script for loading the transformed data into the PostgreSQL database
- `config.py`: Configuration file for API keys and database credentials
- Note: `Apache Airflow` is used for workflow management and scheduling

## Running the ETL Pipeline
After setting up Airflow via Docker:
1. Start the Airflow services (`docker-compose up` or as configured).
2. Open the Airflow web UI at [http://localhost:8080](http://localhost:8080).
3. Locate the DAG named `etl_pipeline`.
4. Toggle the DAG to "on."
5. Trigger it manually or wait for the scheduled run.

## This will:
- Extract drug data from the FDA NDC API
- Transform and clean the data
- Load the results into a PostgreSQL database (running via Docker)