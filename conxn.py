import pyodbc 
import sqlalchemy as sa 
from sqlalchemy import create_engine 
import urllib 

  
conn = urllib.parse.quote_plus( 
    'Data Source Name=MSSQLSERVER01;' 
    'Driver={SQL Server};' 
    'Server=MAEREG\MSSQLSERVER01;' 
    'Database=MSSQLTIPS;' 
    'Trusted_connection=yes;' 
    
) 
coxn = create_engine('mssql+pyodbc:///?odbc_connect={}'.format(conn)) 