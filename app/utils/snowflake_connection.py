from snowflake.snowpark import Session
import os

def create_session():

    connection_parameters = {
        "account": "pu53928.ap-southeast-1",
        "user": "RITESHSAHOO",
        "password": os.getenv("SNOWFLAKE_PASSWORD"),
        "role": "ACCOUNTADMIN",
        "warehouse": "COMPUTE_WH",
        "database": "HAQ_SAHAYAK_DB",
        "schema": "CURATED"
    }

    return Session.builder.configs(connection_parameters).create()