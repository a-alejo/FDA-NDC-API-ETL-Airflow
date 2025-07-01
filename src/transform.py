import psycopg2


def transform_data(**context):
    conn = psycopg2.connect(
        host="postgres",
        database="airflow",
        user="airflow",
        password="airflow",
    )

    cursor = conn.cursor()

    # create the table
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS FDA_Drugs_db (
            product_ndc VARCHAR,
            generic_name TEXT,
            labeler_name TEXT,
            brand_name TEXT,
            active_ingredients JSON,  -- This needs to be serialized
            finished BOOLEAN,
            packaging JSON,  -- This needs to be serialized. Breakup formatting and make FK
            listing_expiration_date DATE,
            openfda JSON, -- This needs to be serialized
            marketing_category VARCHAR,
            dosage_form VARCHAR,
            spl_id VARCHAR,
            product_type VARCHAR,
            route TEXT[],
            marketing_start_date DATE,
            product_id VARCHAR PRIMARY KEY,
            application_number VARCHAR,
            brand_name_base VARCHAR,
            pharm_class TEXT[],  -- This needs to be serialized
            etl_run_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                                                );
    """
    )
    # Commit
    conn.commit()
    conn.close()
