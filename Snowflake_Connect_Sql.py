#It connects to the snowflake account and print the result of the sql query

import pandas as pd
import snowflake.connector
import getpass
pwd = getpass.getpass("Enter password")
conn = snowflake.connector.connect(user='<username>',password=str(pwd),account='<account>.us-east-2.aws')
sql = 'select * from "PRACTICE"."PUBLIC"."HIER"'
res = conn.cursor().execute(sql).fetchall()
df = pd.read_sql(sql,conn)
print(df)
