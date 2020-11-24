# %%
# Here, we are fetching the participants query history from big query in real time. 
# The data that we are fetching includes user email ( aka. user id ), total_bytes_processed, creation_time, start_time, end_time


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
# data.head()

# %%
# From the above data, below are the list of users using Google Big Query 

# 1   ykmavxrc6ftqplrgfcc1kmsqsb83@ironhacks-covid19...
# 2   u3y7f6ahmmr49vqu5euzhxdzniv2@ironhacks-covid19...
# 3   a1mgmiuz4m5g5fy8mgxte8f2exvy2@ironhacks-covid1...
# 4   id-aelytw66irhgplckx0fd8tdetd2@ironhacks-covid...
# 5   qxrin5b06atbzj0295lwbxq6iib2@ironhacks-covid19...
# 8   mjljjomzwsubz2oo7cst9ulwqyg2@ironhacks-covid19...
# 12  welxkvo98jbifcasj9ds76grh3f2@ironhacks-covid19...
# 14  i0qlsyrzkhmjrl7u4f86ikyddlg1@ironhacks-covid19...
# 22  qdmbrejowhhusi9mtqe0m7pgcyb2@ironhacks-covid19...


# So far we have in total of 9 users using Google Big Query 




# %%


# %%
# Here, we are fetching the participants query history from big query in real time. 
# The data that we are fetching includes user email ( aka. user id ), total_bytes_processed, creation_time, start_time, end_time


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
   job_id,
   user_email,
   total_bytes_processed
 FROM `region-us`.INFORMATION_SCHEMA.JOBS_BY_PROJECT
 ORDER BY total_bytes_processed DESC



"""

query_job = bigquery_client.query(QUERY)
import pandas as pd
pd.options.display.max_rows
data = query_job.to_dataframe()
pd.set_option('display.max_rows', None)
print(data)
# data.head()

# %%
# Here, we are fetching the participants query history from big query in real time. 
# The data that we are fetching includes user email ( aka. user id ), total_bytes_processed, creation_time, start_time, end_time


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
   job_id,
   creation_time,
   query
 FROM `region-us`.INFORMATION_SCHEMA.JOBS_BY_PROJECT



"""

query_job = bigquery_client.query(QUERY)
import pandas as pd
pd.options.display.max_rows
data = query_job.to_dataframe()
pd.set_option('display.max_rows', None)
print(data)
# data.head()

# %%
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
   user_email, 
   total_bytes_processed,
   creation_time,
   query
 FROM `region-us`.INFORMATION_SCHEMA.JOBS_BY_PROJECT
 WHERE user_email = "jialincheoh9@gmail.com"




"""

query_job = bigquery_client.query(QUERY)
import pandas as pd
pd.options.display.max_rows
data = query_job.to_dataframe()
pd.set_option('display.max_rows', None)
print(data)
# data.head()


# %%
# This is the information regarding user with user id = ykmavxrc6ftqplrgfcc1kmsqsb83


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
   user_email, 
   total_bytes_processed,
   creation_time,
   query
 FROM `region-us`.INFORMATION_SCHEMA.JOBS_BY_PROJECT
 WHERE user_email = "ykmavxrc6ftqplrgfcc1kmsqsb83@ironhacks-covid19-data.iam.gserviceaccount.com"




"""

query_job = bigquery_client.query(QUERY)
import pandas as pd
pd.options.display.max_rows
data = query_job.to_dataframe()
pd.set_option('display.max_rows', None)
print(data)
# data.head()


# %%
# This is the information regarding user with user id = ykmavxrc6ftqplrgfcc1kmsqsb83


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
   SUM(total_bytes_processed)
 FROM `region-us`.INFORMATION_SCHEMA.JOBS_BY_PROJECT
 WHERE user_email = "ykmavxrc6ftqplrgfcc1kmsqsb83@ironhacks-covid19-data.iam.gserviceaccount.com"




"""

query_job = bigquery_client.query(QUERY)
import pandas as pd
pd.options.display.max_rows
data = query_job.to_dataframe()
pd.set_option('display.max_rows', None)
print(data)
# data.head()

# %%
# This is the information regarding user with user id = ykmavxrc6ftqplrgfcc1kmsqsb83


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
   SUM(total_bytes_processed)
 FROM `region-us`.INFORMATION_SCHEMA.JOBS_BY_PROJECT
 WHERE user_email = "ykmavxrc6ftqplrgfcc1kmsqsb83@ironhacks-covid19-data.iam.gserviceaccount.com"




"""

query_job = bigquery_client.query(QUERY)
import pandas as pd
pd.options.display.max_rows
data = query_job.to_dataframe()
pd.set_option('display.max_rows', None)
print(data)
# data.head()

# %%
# This is the information regarding user with user id = u3y7f6ahmmr49vqu5euzhxdzniv2


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
   user_email, 
   total_bytes_processed,
   creation_time,
   query
 FROM `region-us`.INFORMATION_SCHEMA.JOBS_BY_PROJECT
 WHERE user_email = "u3y7f6ahmmr49vqu5euzhxdzniv2@ironhacks-covid19-data.iam.gserviceaccount.com"




"""

query_job = bigquery_client.query(QUERY)
import pandas as pd
pd.options.display.max_rows
data_1 = query_job.to_dataframe()
pd.set_option('display.max_rows', None)
print(data_1)
# data.head()



# %%
# This is the information regarding user with user id = a1mgmiuz4m5g5fy8mgxte8f2exvy2


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
   user_email, 
   total_bytes_processed,
   creation_time,
   query
 FROM `region-us`.INFORMATION_SCHEMA.JOBS_BY_PROJECT
 WHERE user_email = "a1mgmiuz4m5g5fy8mgxte8f2exvy2@ironhacks-covid19-data.iam.gserviceaccount.com"




"""

query_job = bigquery_client.query(QUERY)
import pandas as pd
pd.options.display.max_rows
data_1 = query_job.to_dataframe()
pd.set_option('display.max_rows', None)
print(data_1)
# data.head()

# %%
# This is the information regarding user with user id = a1mgmiuz4m5g5fy8mgxte8f2exvy2


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
   SUM(total_bytes_processed)
 FROM `region-us`.INFORMATION_SCHEMA.JOBS_BY_PROJECT
 WHERE user_email = "a1mgmiuz4m5g5fy8mgxte8f2exvy2@ironhacks-covid19-data.iam.gserviceaccount.com"




"""

query_job = bigquery_client.query(QUERY)
import pandas as pd
pd.options.display.max_rows
data_18 = query_job.to_dataframe()
pd.set_option('display.max_rows', None)
print(data_18)
# data.head()

# %%
# This is the information regarding user with user id = id-aelytw66irhgplckx0fd8tdetd2


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
   user_email, 
   total_bytes_processed,
   creation_time,
   query
 FROM `region-us`.INFORMATION_SCHEMA.JOBS_BY_PROJECT
 WHERE user_email = "id-aelytw66irhgplckx0fd8tdetd2@ironhacks-covid19-data.iam.gserviceaccount.com"




"""

query_job = bigquery_client.query(QUERY)
import pandas as pd
pd.options.display.max_rows
data_1 = query_job.to_dataframe()
pd.set_option('display.max_rows', None)
print(data_1)
# data.head()

# %%
# This is the information regarding user with user id = id-aelytw66irhgplckx0fd8tdetd2


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
   SUM(total_bytes_processed)
 FROM `region-us`.INFORMATION_SCHEMA.JOBS_BY_PROJECT
 WHERE user_email = "id-aelytw66irhgplckx0fd8tdetd2@ironhacks-covid19-data.iam.gserviceaccount.com"




"""

query_job = bigquery_client.query(QUERY)
import pandas as pd
pd.options.display.max_rows
data_1 = query_job.to_dataframe()
pd.set_option('display.max_rows', None)
print(data_1)
# data.head()

# %%
# This is the information regarding user with user id =  qxrin5b06atbzj0295lwbxq6iib2


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
   user_email, 
   total_bytes_processed,
   creation_time,
   query
 FROM `region-us`.INFORMATION_SCHEMA.JOBS_BY_PROJECT
 WHERE user_email = "qxrin5b06atbzj0295lwbxq6iib2@ironhacks-covid19-data.iam.gserviceaccount.com"




"""

query_job = bigquery_client.query(QUERY)
import pandas as pd
pd.options.display.max_rows
data_1 = query_job.to_dataframe()
pd.set_option('display.max_rows', None)
print(data_1)
# data.head()

# %%
# This is the information regarding user with user id =  qxrin5b06atbzj0295lwbxq6iib2


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
   SUM(total_bytes_processed)
 FROM `region-us`.INFORMATION_SCHEMA.JOBS_BY_PROJECT
 WHERE user_email = "qxrin5b06atbzj0295lwbxq6iib2@ironhacks-covid19-data.iam.gserviceaccount.com"




"""

query_job = bigquery_client.query(QUERY)
import pandas as pd
pd.options.display.max_rows
data_1 = query_job.to_dataframe()
pd.set_option('display.max_rows', None)
print(data_1)
# data.head()

# %%
# This is the information regarding user with user id =  mjljjomzwsubz2oo7cst9ulwqyg2


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
   user_email, 
   total_bytes_processed,
   creation_time,
   query
 FROM `region-us`.INFORMATION_SCHEMA.JOBS_BY_PROJECT
 WHERE user_email = "mjljjomzwsubz2oo7cst9ulwqyg2@ironhacks-covid19-data.iam.gserviceaccount.com"




"""

query_job = bigquery_client.query(QUERY)
import pandas as pd
pd.options.display.max_rows
data_1 = query_job.to_dataframe()
pd.set_option('display.max_rows', None)
print(data_1)
# data.head()

# %%
# This is the information regarding user with user id =  mjljjomzwsubz2oo7cst9ulwqyg2


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
   SUM(total_bytes_processed)
 FROM `region-us`.INFORMATION_SCHEMA.JOBS_BY_PROJECT
 WHERE user_email = "mjljjomzwsubz2oo7cst9ulwqyg2@ironhacks-covid19-data.iam.gserviceaccount.com"




"""

query_job = bigquery_client.query(QUERY)
import pandas as pd
pd.options.display.max_rows
data_16 = query_job.to_dataframe()
pd.set_option('display.max_rows', None)
print(data_16)
# data.head()

# %%
# This is the information regarding user with user id =   welxkvo98jbifcasj9ds76grh3f2


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
   user_email, 
   total_bytes_processed,
   creation_time,
   query
 FROM `region-us`.INFORMATION_SCHEMA.JOBS_BY_PROJECT
 WHERE user_email = "welxkvo98jbifcasj9ds76grh3f2@ironhacks-covid19-data.iam.gserviceaccount.com"




"""

query_job = bigquery_client.query(QUERY)
import pandas as pd
pd.options.display.max_rows
data_1 = query_job.to_dataframe()
pd.set_option('display.max_rows', None)
print(data_1)
# data.head()

# %%
# This is the information regarding user with user id =   welxkvo98jbifcasj9ds76grh3f2


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
   SUM(total_bytes_processed)
 FROM `region-us`.INFORMATION_SCHEMA.JOBS_BY_PROJECT
 WHERE user_email = "welxkvo98jbifcasj9ds76grh3f2@ironhacks-covid19-data.iam.gserviceaccount.com"




"""

query_job = bigquery_client.query(QUERY)
import pandas as pd
pd.options.display.max_rows
data_1 = query_job.to_dataframe()
pd.set_option('display.max_rows', None)
print(data_1)
# data.head()

# %%
# This is the information regarding user with user id =   i0qlsyrzkhmjrl7u4f86ikyddlg1


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
   user_email, 
   total_bytes_processed,
   creation_time,
   query
 FROM `region-us`.INFORMATION_SCHEMA.JOBS_BY_PROJECT
 WHERE user_email = "i0qlsyrzkhmjrl7u4f86ikyddlg1@ironhacks-covid19-data.iam.gserviceaccount.com"




"""

query_job = bigquery_client.query(QUERY)
import pandas as pd
pd.options.display.max_rows
data_1 = query_job.to_dataframe()
pd.set_option('display.max_rows', None)
print(data_1)
# data.head()

# %%
# This is the information regarding user with user id =   i0qlsyrzkhmjrl7u4f86ikyddlg1


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
   SUM(total_bytes_processed)
 FROM `region-us`.INFORMATION_SCHEMA.JOBS_BY_PROJECT
 WHERE user_email = "i0qlsyrzkhmjrl7u4f86ikyddlg1@ironhacks-covid19-data.iam.gserviceaccount.com"




"""

query_job = bigquery_client.query(QUERY)
import pandas as pd
pd.options.display.max_rows
data_13 = query_job.to_dataframe()
pd.set_option('display.max_rows', None)
print(data_13)
# data.head()

# %%
# This is the information regarding user with user id =  nztjlzmrp1dv6p9vdcum1aob27m2


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
   user_email, 
   total_bytes_processed,
   creation_time,
   query
 FROM `region-us`.INFORMATION_SCHEMA.JOBS_BY_PROJECT
 WHERE user_email = "nztjlzmrp1dv6p9vdcum1aob27m2@ironhacks-covid19-data.iam.gserviceaccount.com"




"""

query_job = bigquery_client.query(QUERY)
import pandas as pd
pd.options.display.max_rows
data_1 = query_job.to_dataframe()
pd.set_option('display.max_rows', None)
print(data_1)
# data.head()

# %%
# This is the information regarding user with user id =  nztjlzmrp1dv6p9vdcum1aob27m2


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
   SUM(total_bytes_processed)
 FROM `region-us`.INFORMATION_SCHEMA.JOBS_BY_PROJECT
 WHERE user_email = "nztjlzmrp1dv6p9vdcum1aob27m2@ironhacks-covid19-data.iam.gserviceaccount.com"




"""

query_job = bigquery_client.query(QUERY)
import pandas as pd
pd.options.display.max_rows
data_11 = query_job.to_dataframe()
pd.set_option('display.max_rows', None)
print(data_11)
# data.head()

# %%
# This is the information regarding user with user id =  qdmbrejowhhusi9mtqe0m7pgcyb2


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
   user_email, 
   total_bytes_processed,
   creation_time,
   query
 FROM `region-us`.INFORMATION_SCHEMA.JOBS_BY_PROJECT
 WHERE user_email = "qdmbrejowhhusi9mtqe0m7pgcyb2@ironhacks-covid19-data.iam.gserviceaccount.com"




"""

query_job = bigquery_client.query(QUERY)
import pandas as pd
pd.options.display.max_rows
data_9 = query_job.to_dataframe()
pd.set_option('display.max_rows', None)
print(data_9)
# data.head()

# %%
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
 SUM(total_bytes_processed)
 FROM `region-us`.INFORMATION_SCHEMA.JOBS_BY_PROJECT
 WHERE user_email = "qdmbrejowhhusi9mtqe0m7pgcyb2@ironhacks-covid19-data.iam.gserviceaccount.com"




"""

query_job = bigquery_client.query(QUERY)
import pandas as pd
pd.options.display.max_rows
data_10 = query_job.to_dataframe()
pd.set_option('display.max_rows', None)
print(data_10)
# data.head()

# %%
data = [['ykmavxrc6ftqplrgfcc1kmsqsb83', 'kaungmyatzaw611@gmail.com', 'Kaung Myat Zaw', 103, 6255622, 0, 0],['u3y7f6ahmmr49vqu5euzhxdzniv2', 'pavuluriharsh@gmail.com', 'Harsha Pavuluri', 40, 6255622],['1mgmiuz4m5g5fy8mgxte8f2exvy2n', 'evelynyshi@gmail.com', 'Evelyn Shi', 23, 2080711], ['2aelytw66irhgplckx0fd8tdetd2', 'fenypatel1999@gmail.com', 'Feny Patel', 520, 1717312], ['qxrin5b06atbzj0295lwbxq6iib2', 'heinzay1999@gmail.com', 'Hein Zay Yar Oo', 118, 1541966], 
        ['mjljjomzwsubz2oo7cst9ulwqyg2', 'melkady@purdue.edu','Mai Elkady', 12, 828192], ['welxkvo98jbifcasj9ds76grh3f2', 'shyhsmq@gmail.com', 'Hanwen Gu', 23,  70528], ['i0qlsyrzkhmjrl7u4f86ikyddlg1', 'zjiao19@outlook.com', 'Ziteng Jiao', 29, 3331008], ['nztjlzmrp1dv6p9vdcum1aob27m2', 'krishn88@purdue.edu', 'Ashwin Krishnaswamy', 40, 63362704], ['qdmbrejowhhusi9mtqe0m7pgcyb2', 'tokalarr@gmail.com', 'Rohit Tokala', 3, 765356], ['']]
df = pd.DataFrame(data,columns=['user_id','email', 'name', 'phase_1_bigquery_jobs', 'phase_1_bigquery_bytes', 'phase_2_bigquery_jobs', 'phase_2_bigquery_bytes'])
df

# %%
df

# %%


# %%
df['Submission Deadline 1'] = 'August 24, 2020'
df

# %%
df.to_csv("phase-1-results.csv")

# %%
# This is the information regarding user with user id =   i0qlsyrzkhmjrl7u4f86ikyddlg1


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
   user_email, 
   total_bytes_processed,
   creation_time,
   query
 FROM `region-us`.INFORMATION_SCHEMA.JOBS_BY_PROJECT
 WHERE user_email = "i0qlsyrzkhmjrl7u4f86ikyddlg1@ironhacks-covid19-data.iam.gserviceaccount.com"




"""

query_job = bigquery_client.query(QUERY)
import pandas as pd
pd.options.display.max_rows
data_1 = query_job.to_dataframe()
pd.set_option('display.max_rows', None)
print(data_1)
# data.head()

# %%
# This is the information regarding user with user id =   i0qlsyrzkhmjrl7u4f86ikyddlg1


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
   SUM(total_bytes_processed)
 FROM `region-us`.INFORMATION_SCHEMA.JOBS_BY_PROJECT
 WHERE user_email = "i0qlsyrzkhmjrl7u4f86ikyddlg1@ironhacks-covid19-data.iam.gserviceaccount.com"




"""

query_job = bigquery_client.query(QUERY)
import pandas as pd
pd.options.display.max_rows
data_1 = query_job.to_dataframe()
pd.set_option('display.max_rows', None)
print(data_1)
# data.head()

# %%
# This is the information regarding user with user id = id-aelytw66irhgplckx0fd8tdetd2


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
   user_email, 
   total_bytes_processed,
   creation_time,
   query
 FROM `region-us`.INFORMATION_SCHEMA.JOBS_BY_PROJECT
 WHERE user_email = "id-aelytw66irhgplckx0fd8tdetd2@ironhacks-covid19-data.iam.gserviceaccount.com"




"""

query_job = bigquery_client.query(QUERY)
import pandas as pd
pd.options.display.max_rows
data_1 = query_job.to_dataframe()
pd.set_option('display.max_rows', None)
print(data_1)
# data.head()

# %%
# This is the information regarding user with user id = id-aelytw66irhgplckx0fd8tdetd2


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
  SUM(total_bytes_processed)
 FROM `region-us`.INFORMATION_SCHEMA.JOBS_BY_PROJECT
 WHERE user_email = "id-aelytw66irhgplckx0fd8tdetd2@ironhacks-covid19-data.iam.gserviceaccount.com"




"""

query_job = bigquery_client.query(QUERY)
import pandas as pd
pd.options.display.max_rows
data_1 = query_job.to_dataframe()
pd.set_option('display.max_rows', None)
print(data_1)
# data.head()

# %%
# This is the information regarding user with user id = a1mgmiuz4m5g5fy8mgxte8f2exvy2


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
   user_email, 
   total_bytes_processed,
   creation_time,
   query
 FROM `region-us`.INFORMATION_SCHEMA.JOBS_BY_PROJECT
 WHERE user_email = "a1mgmiuz4m5g5fy8mgxte8f2exvy2@ironhacks-covid19-data.iam.gserviceaccount.com"




"""

query_job = bigquery_client.query(QUERY)
import pandas as pd
pd.options.display.max_rows
data_1 = query_job.to_dataframe()
pd.set_option('display.max_rows', None)
print(data_1)
# data.head()

# %%
# This is the information regarding user with user id = a1mgmiuz4m5g5fy8mgxte8f2exvy2


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
   SUM(total_bytes_processed)
 FROM `region-us`.INFORMATION_SCHEMA.JOBS_BY_PROJECT
 WHERE user_email = "a1mgmiuz4m5g5fy8mgxte8f2exvy2@ironhacks-covid19-data.iam.gserviceaccount.com"




"""

query_job = bigquery_client.query(QUERY)
import pandas as pd
pd.options.display.max_rows
data_1 = query_job.to_dataframe()
pd.set_option('display.max_rows', None)
print(data_1)
# data.head()

# %%
# This is the information regarding user with user id = dvebmrzw


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
   user_email, 
   total_bytes_processed,
   creation_time,
   query
 FROM `region-us`.INFORMATION_SCHEMA.JOBS_BY_PROJECT
 WHERE user_email = "dvebmrzw@ironhacks-covid19-data.iam.gserviceaccount.com"




"""

query_job = bigquery_client.query(QUERY)
import pandas as pd
pd.options.display.max_rows
data_1 = query_job.to_dataframe()
pd.set_option('display.max_rows', None)
print(data_1)
# data.head()

# %%
df['Submission Deadline 2'] = 'Sept 1, 2020'
df

# %%
data = [['ykmavxrc6ftqplrgfcc1kmsqsb83', 'kaungmyatzaw611@gmail.com', 'Kaung Myat Zaw', 103, 6255622, 0, 0],['u3y7f6ahmmr49vqu5euzhxdzniv2', 'pavuluriharsh@gmail.com', 'Harsha Pavuluri', 40, 6255622],['1mgmiuz4m5g5fy8mgxte8f2exvy2n', 'evelynyshi@gmail.com', 'Evelyn Shi', 23, 2080711], ['2aelytw66irhgplckx0fd8tdetd2', 'fenypatel1999@gmail.com', 'Feny Patel', 48, 1717312, 568], ['qxrin5b06atbzj0295lwbxq6iib2', 'heinzay1999@gmail.com', 'Hein Zay Yar Oo', 118, 1541966], 
        ['mjljjomzwsubz2oo7cst9ulwqyg2', 'melkady@purdue.edu','Mai Elkady', 12, 828192], ['welxkvo98jbifcasj9ds76grh3f2', 'shyhsmq@gmail.com', 'Hanwen Gu', 23,  70528], ['i0qlsyrzkhmjrl7u4f86ikyddlg1', 'zjiao19@outlook.com', 'Ziteng Jiao', 29, 3331008], ['nztjlzmrp1dv6p9vdcum1aob27m2', 'krishn88@purdue.edu', 'Ashwin Krishnaswamy', 40, 63362704], ['qdmbrejowhhusi9mtqe0m7pgcyb2', 'tokalarr@gmail.com', 'Rohit Tokala', 3, 765356]]
df = pd.DataFrame(data,columns=['user_id','email', 'name', 'phase_1_bigquery_jobs', 'phase_1_bigquery_bytes', 'phase_2_bigquery_jobs', 'phase_2_bigquery_bytes'])
df

# %%
data = [['ykmavxrc6ftqplrgfcc1kmsqsb83', 'kaungmyatzaw611@gmail.com', 'Kaung Myat Zaw', 0, 0, 103, 6255622],['u3y7f6ahmmr49vqu5euzhxdzniv2', 'pavuluriharsh@gmail.com', 'Harsha Pavuluri', 0, 0, 40, 6255622],['1mgmiuz4m5g5fy8mgxte8f2exvy2n', 'evelynyshi@gmail.com', 'Evelyn Shi', 53, 2703733, 76, 4784444 ], ['2aelytw66irhgplckx0fd8tdetd2', 'fenypatel1999@gmail.com', 'Feny Patel', 48, 1450399, 568, 3167711], ['qxrin5b06atbzj0295lwbxq6iib2', 'heinzay1999@gmail.com', 'Hein Zay Yar Oo', 0, 0, 118, 1541966], 
        ['mjljjomzwsubz2oo7cst9ulwqyg2', 'melkady@purdue.edu','Mai Elkady', 0, 0, 12, 828192], ['welxkvo98jbifcasj9ds76grh3f2', 'shyhsmq@gmail.com', 'Hanwen Gu', 0, 0, 23,  70528], ['i0qlsyrzkhmjrl7u4f86ikyddlg1', 'zjiao19@outlook.com', 'Ziteng Jiao', 28, 916453, 57, 4247461], ['nztjlzmrp1dv6p9vdcum1aob27m2', 'krishn88@purdue.edu', 'Ashwin Krishnaswamy', 0, 0, 40, 63362704], ['qdmbrejowhhusi9mtqe0m7pgcyb2', 'tokalarr@gmail.com', 'Rohit Tokala', 0, 0, 3, 765356]]
df = pd.DataFrame(data,columns=['user_id','email', 'name', 'phase_2_bigquery_jobs', 'phase_2_bigquery_bytes', 'cum_phase2_jobs', 'cum_phase2_bytes'])
df

# %%
df.to_csv("phase-2-results.csv")

# %%
# This is the information regarding user with user id = id-aelytw66irhgplckx0fd8tdetd2


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
  SUM(total_bytes_processed)
 FROM `region-us`.INFORMATION_SCHEMA.JOBS_BY_PROJECT
 WHERE user_email = "id-aelytw66irhgplckx0fd8tdetd2@ironhacks-covid19-data.iam.gserviceaccount.com"




"""

query_job = bigquery_client.query(QUERY)
import pandas as pd
pd.options.display.max_rows
data_1 = query_job.to_dataframe()
pd.set_option('display.max_rows', None)
print(data_1)
# data.head()

# %%
# This is the information regarding user with user id = a1mgmiuz4m5g5fy8mgxte8f2exvy2


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
   user_email, 
   total_bytes_processed,
   creation_time,
   query
 FROM `region-us`.INFORMATION_SCHEMA.JOBS_BY_PROJECT
 WHERE user_email = "a1mgmiuz4m5g5fy8mgxte8f2exvy2@ironhacks-covid19-data.iam.gserviceaccount.com"




"""

query_job = bigquery_client.query(QUERY)
import pandas as pd
pd.options.display.max_rows
data_1 = query_job.to_dataframe()
pd.set_option('display.max_rows', None)
print(data_1)
# data.head()

# %%
# This is the information regarding user with user id = a1mgmiuz4m5g5fy8mgxte8f2exvy2


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
   SUM(total_bytes_processed)
 FROM `region-us`.INFORMATION_SCHEMA.JOBS_BY_PROJECT
 WHERE user_email = "a1mgmiuz4m5g5fy8mgxte8f2exvy2@ironhacks-covid19-data.iam.gserviceaccount.com"




"""

query_job = bigquery_client.query(QUERY)
import pandas as pd
pd.options.display.max_rows
data_1 = query_job.to_dataframe()
pd.set_option('display.max_rows', None)
print(data_1)
# data.head()

# %%
# This is the information regarding user with user id =   i0qlsyrzkhmjrl7u4f86ikyddlg1


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
   SUM(total_bytes_processed)
 FROM `region-us`.INFORMATION_SCHEMA.JOBS_BY_PROJECT
 WHERE user_email = "i0qlsyrzkhmjrl7u4f86ikyddlg1@ironhacks-covid19-data.iam.gserviceaccount.com"




"""

query_job = bigquery_client.query(QUERY)
import pandas as pd
pd.options.display.max_rows
data_1 = query_job.to_dataframe()
pd.set_option('display.max_rows', None)
print(data_1)
# data.head()

# %%
# This is the information regarding user with user id =   i0qlsyrzkhmjrl7u4f86ikyddlg1


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
   total_bytes_processed
 FROM `region-us`.INFORMATION_SCHEMA.JOBS_BY_PROJECT
 WHERE user_email = "i0qlsyrzkhmjrl7u4f86ikyddlg1@ironhacks-covid19-data.iam.gserviceaccount.com"




"""

query_job = bigquery_client.query(QUERY)
import pandas as pd
pd.options.display.max_rows
data_1 = query_job.to_dataframe()
pd.set_option('display.max_rows', None)
print(data_1)
# data.head()

# %%
# This is the information regarding user with user id =  mjljjomzwsubz2oo7cst9ulwqyg2


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
   query
 FROM `region-us`.INFORMATION_SCHEMA.JOBS_BY_PROJECT
 WHERE user_email = "mjljjomzwsubz2oo7cst9ulwqyg2@ironhacks-covid19-data.iam.gserviceaccount.com"




"""

query_job = bigquery_client.query(QUERY)
import pandas as pd
pd.options.display.max_rows
data_1 = query_job.to_dataframe()
pd.set_option('display.max_rows', None)
print(data_1)
# data.head()

# %%
# This is the information regarding user with user id =  mjljjomzwsubz2oo7cst9ulwqyg2


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
   SUM(total_bytes_processed)
 FROM `region-us`.INFORMATION_SCHEMA.JOBS_BY_PROJECT
 WHERE user_email = "mjljjomzwsubz2oo7cst9ulwqyg2@ironhacks-covid19-data.iam.gserviceaccount.com"




"""

query_job = bigquery_client.query(QUERY)
import pandas as pd
pd.options.display.max_rows
data_1 = query_job.to_dataframe()
pd.set_option('display.max_rows', None)
print(data_1)
# data.head()

# %%
# This is the information regarding user with user id =  qxrin5b06atbzj0295lwbxq6iib2


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
   SUM(total_bytes_processed)
 FROM `region-us`.INFORMATION_SCHEMA.JOBS_BY_PROJECT
 WHERE user_email = "qxrin5b06atbzj0295lwbxq6iib2@ironhacks-covid19-data.iam.gserviceaccount.com"




"""

query_job = bigquery_client.query(QUERY)
import pandas as pd
pd.options.display.max_rows
data_1 = query_job.to_dataframe()
pd.set_option('display.max_rows', None)
print(data_1)
# data.head()

# %%
# This is the information regarding user with user id =  mjljjomzwsubz2oo7cst9ulwqyg2


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
   user_email, 
   total_bytes_processed,
   creation_time,
   query
 FROM `region-us`.INFORMATION_SCHEMA.JOBS_BY_PROJECT
 WHERE user_email = "qxrin5b06atbzj0295lwbxq6iib2@ironhacks-covid19-data.iam.gserviceaccount.com"




"""

query_job = bigquery_client.query(QUERY)
import pandas as pd
pd.options.display.max_rows
data_1 = query_job.to_dataframe()
pd.set_option('display.max_rows', None)
print(data_1)
# data.head()

# %%
# This is the information regarding user with user id = u3y7f6ahmmr49vqu5euzhxdzniv2


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
   user_email, 
   total_bytes_processed,
   creation_time,
   query
 FROM `region-us`.INFORMATION_SCHEMA.JOBS_BY_PROJECT
 WHERE user_email = "u3y7f6ahmmr49vqu5euzhxdzniv2@ironhacks-covid19-data.iam.gserviceaccount.com"




"""

query_job = bigquery_client.query(QUERY)
import pandas as pd
pd.options.display.max_rows
data_1 = query_job.to_dataframe()
pd.set_option('display.max_rows', None)
print(data_1)
# data.head()

# %%
# This is the information regarding user with user id =  qxrin5b06atbzj0295lwbxq6iib2


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
   SUM(total_bytes_processed)
 FROM `region-us`.INFORMATION_SCHEMA.JOBS_BY_PROJECT
 WHERE user_email = "qxrin5b06atbzj0295lwbxq6iib2@ironhacks-covid19-data.iam.gserviceaccount.com"




"""

query_job = bigquery_client.query(QUERY)
import pandas as pd
pd.options.display.max_rows
data_1 = query_job.to_dataframe()
pd.set_option('display.max_rows', None)
print(data_1)
# data.head()

# %%
# This is the information regarding user with user id =   i0qlsyrzkhmjrl7u4f86ikyddlg1


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
   query
 FROM `region-us`.INFORMATION_SCHEMA.JOBS_BY_PROJECT
 WHERE user_email = "i0qlsyrzkhmjrl7u4f86ikyddlg1@ironhacks-covid19-data.iam.gserviceaccount.com"




"""

query_job = bigquery_client.query(QUERY)
import pandas as pd
pd.options.display.max_rows
data_1 = query_job.to_dataframe()
pd.set_option('display.max_rows', None)
print(data_1)
# data.head()

# %%
# This is the information regarding user with user id =   i0qlsyrzkhmjrl7u4f86ikyddlg1


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
   SUM(total_bytes_processed)
 FROM `region-us`.INFORMATION_SCHEMA.JOBS_BY_PROJECT
 WHERE user_email = "i0qlsyrzkhmjrl7u4f86ikyddlg1@ironhacks-covid19-data.iam.gserviceaccount.com"




"""

query_job = bigquery_client.query(QUERY)
import pandas as pd
pd.options.display.max_rows
data_1 = query_job.to_dataframe()
pd.set_option('display.max_rows', None)
print(data_1)
# data.head()

# %%
# This is the information regarding user with user id =   i0qlsyrzkhmjrl7u4f86ikyddlg1


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
   query
 FROM `region-us`.INFORMATION_SCHEMA.JOBS_BY_PROJECT
 WHERE user_email = "i0qlsyrzkhmjrl7u4f86ikyddlg1@ironhacks-covid19-data.iam.gserviceaccount.com"




"""

query_job = bigquery_client.query(QUERY)
import pandas as pd
pd.options.display.max_rows
data_1 = query_job.to_dataframe()
pd.set_option('display.max_rows', None)
print(data_1)
# data.head()

# %%
