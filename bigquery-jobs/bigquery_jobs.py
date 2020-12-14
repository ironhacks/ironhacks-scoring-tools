#!/usr/bin/env python3

import os
import pprint
from google.cloud import bigquery
from google.oauth2 import service_account

BQ_PROJECT = 'ironhacks-covid19-data'
BQ_KEYFILE = 'service_account.json'

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = BQ_KEYFILE

bigquery_client = bigquery.Client(project=BQ_PROJECT)

QUERY = """
SELECT
  user_email,
  COUNT(user_email) as job_count
FROM `region-us`.INFORMATION_SCHEMA.JOBS_BY_PROJECT
WHERE creation_time > '2020-11-22'
GROUP BY user_email
ORDER BY job_count DESC
"""

query_job = bigquery_client.query(QUERY)

data = query_job.to_dataframe()

print(data)
