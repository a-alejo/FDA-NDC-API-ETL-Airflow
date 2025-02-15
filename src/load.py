import json
import psycopg2
from config import db_user, db_password


def load_data():
    conn = psycopg2.connect(
        host = 'localhost',
        database = 'Postgres 16 - Localhost - FDA-NDC-ETL_db',
        user = db_user,
        password = db_password)

    cursor = conn.cursor()

    # Using a manual approach for data extraction and handling to break out each item for SQL insertion instead of relying on pd.json_normalize
    for result in all_results:
        product_ndc = result.get('product_ndc')
        generic_name = result.get('generic_name')
        labeler_name = result.get('labeler_name')
        brand_name = result.get('brand_name')
        active_ingredients = json.dumps(result.get('active_ingredients'))  # this is a dictionary
        finished = result.get('finished')
        packaging = json.dumps(result.get('packaging'))  # this is a dictionary
        listing_expiration_date = result.get('listing_expiration_date')
        openfda = json.dumps(result.get('openfda')) # this is a dictionary
        marketing_category = result.get('marketing_category')
        dosage_form = result.get('dosage_form')
        spl_id = result.get('spl_id')
        product_type = result.get('product_type')
        route = result.get('route')
        marketing_start_date = result.get('marketing_start_date')
        product_id = result.get('product_id')
        application_number = result.get('application_number')
        brand_name_base = result.get('brand_name_base')
        pharm_class = result.get('pharm_class') # this is a dictionary


        # Add data to the table
        cursor.execute(
            '''
            INSERT INTO FDA_Drugs_db (
            "product_ndc",
            "generic_name",
            "labeler_name",
            "brand_name",
            "active_ingredients",
            "finished",
            "packaging",
            "listing_expiration_date",
            "openfda",
            "marketing_category",
            "dosage_form",
            "spl_id",
            "product_type",
            "route",
            "marketing_start_date",
            "product_id",
            "application_number",
            "brand_name_base",
            "pharm_class"
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        ON CONFLICT ("product_id") DO NOTHING
            ''', 
            (
                product_ndc,
                generic_name,
                labeler_name,
                brand_name,
                active_ingredients,
                finished,
                packaging,
                listing_expiration_date,
                openfda,
                marketing_category,
                dosage_form,
                spl_id,
                product_type,
                route,
                marketing_start_date,
                product_id,
                application_number,
                brand_name_base,
                pharm_class
            )
        )

        # Commit the transaction
        conn.commit()
        conn.close()
    print("Data inserted successfully")