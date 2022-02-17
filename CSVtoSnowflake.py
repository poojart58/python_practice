#This program is to load the data into the snowflake table using python and Pandas

import pandas
import snowflake.connector as snow
from snowflake.connector.pandas_tools import write_pandas


conn = snow.connect(
    user='<user>',
    password='<password>',
    account='<account_name>',
    warehouse='<Warehouse>',
          database='<Database name>',
          schema='<Schema Name>',
    protocol='https',
          port=443
    )

# This is to check if the connection is sucessful or not 
cur = conn.cursor()
cur.close()


original = "/Users/<name>/Desktop/Cust_Data/Cust_Data.csv"  #Define the path of your file
delimiter = "," 

total = pd.read_csv(original, delimiter=',')

#The below code is used when the column name in file is different than column name in snowflake table

total.rename(columns={"id": "ID", 
                       "Name": "NAME",
                     "Salary": "SALARY"},
                        inplace=True)

write_pandas(conn, total, "CUST") # CUST is the table name present in snowflake DB

