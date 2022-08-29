#importing modules 
import requests 
import pandas as pd 
from pandas import json_normalize 
from conxn import coxn 
  
#defining headers 
headers = { 
    'accept':'application/json', 
} 
#defining baseurl 
baseurl = 'https://jsonplaceholder.typicode.com/' 
#defining endpoint 
endpoint  = 'users' 
  
#main request function 
def main_request(baseurl,endpoint,headers): 
        #using requests to call API data 
        r = requests.get(baseurl + endpoint,headers=headers) 
        #returning data in json format 
        return r.json() 
  
#variable calling main function 
data = main_request(baseurl=baseurl,endpoint=endpoint,headers=headers) 
#creating a dataframe using pandas 
data_DF = pd.DataFrame(data) 
  
#adding a column called index to dataframe 
data_DF['index'] = range(0,len(data_DF)) 
    
#creating a different dataframe for the nested column 
company_DF = pd.concat([pd.DataFrame(json_normalize(x)) for x in data_DF['company']],sort=False) 
#Renaming the column names to include company_ prefix 
company_DF.columns = 'company_' + company_DF.columns 
#creating a new column called index 
company_DF['index'] = range(0, len(company_DF)) 
    
#combining the original dataframe with the dataframe from nested column. 
merged_df = pd.merge(data_DF,company_DF,on="index") 
#dropping the address column 
merged_df = merged_df.drop(['address'], axis=1) 
#dropping the company 
merged_df = merged_df.drop(['company'], axis=1) 
#write out merged data 
print(merged_df) 
  
#Added code to enable writing to SQL database. 
merged_df.to_sql('Users',con=coxn, schema='dbo', if_exists='replace',index=True) 