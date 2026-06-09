from snowflake.snowpark import Session
import os

def create_session():

    connection_parameters = {
        "account": "yt25244.ap-southeast-1",
        "user": "RITESH",
        "password": os.getenv("SNOWFLAKE_PASSWORD"),
        "role": "ACCOUNTADMIN",
        "warehouse": "COMPUTE_WH",
        "database": "HAQ_SAHAYAK_DB",
        "schema": "CURATED"
    }

    return Session.builder.configs(connection_parameters).create()