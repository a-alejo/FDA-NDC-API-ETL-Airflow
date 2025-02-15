import os
from dotenv import load_dotenv

# load credentials
load_dotenv()

db_user = os.getenv("db_user")
db_password = os.getenv("db_password")
api_key = os.getenv("api_key")
