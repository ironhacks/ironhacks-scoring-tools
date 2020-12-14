!python3 -m pip install google.cloud
from google.cloud import bigquery
from google.oauth2 import service_account
from google.cloud.bigquery import magics
import os
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] ='/home/jovyan/ironhacks.json'
bigquery_client = bigquery.Client(project='ironhacks-covid19-data')
bigquery_client
bigquery_client = bigquery.Client()



QUERY = """
SELECT
   DISTINCT(user_email) AS user
 FROM
   `region-us`.INFORMATION_SCHEMA.JOBS_BY_PROJECT
 WHERE
   job_type = "QUERY"
"""

query_job = bigquery_client.query(QUERY)
import pandas as pd
pd.options.display.max_rows
data = query_job.to_dataframe()
pd.set_option('display.max_rows', None)
print(data)
