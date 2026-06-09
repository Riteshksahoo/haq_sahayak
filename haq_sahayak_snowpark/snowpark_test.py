from snowflake.snowpark import Session
import os
#Connection initialization:

connection_parameters = {
    "account": "yt25244.ap-southeast-1",
    "user": "RITESH",
    "password": os.getenv("SNOWFLAKE_PASSWORD"),
    "role": "ACCOUNTADMIN",
    "warehouse": "COMPUTE_WH",
    "database": "HAQ_SAHAYAK_DB",
    "schema": "CURATED"
}
session = Session.builder.configs(connection_parameters).create()
print("Connected Successfully!")
print()

#Read Tables:

applications_df = session.table("CITIZEN_APPLICATIONS")
print("CITIZEN_APPLICATIONS DATA")
applications_df.show()

#Total Applications:

print("Total Applications :", applications_df.count())
print()

#Application By Status:

print("APPLICATIONS BY STATUS")
status_df = (
    applications_df
    .group_by("STATUS")
    .count()
)
status_df.show()

#Join With Processes:

print("APPLICATIONS WITH PROCESS DETAILS")
process_df = session.table("PROCESSES")
joined_df = (
    applications_df.join(
        process_df,
        applications_df["PROCESS_ID"] == process_df["PROCESS_ID"]
    )
)
joined_df.show()

#Session Close:

session.close()
print("Snowflake Session Closed")