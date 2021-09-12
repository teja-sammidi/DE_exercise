
import sys
import pandas as pd
import json
import filepath
from os import getenv

def read_component_file_to_dataframe():
    try:
        components_df=pd.read_csv(getenv('file_path') + 'components.csv')
        return components_df
    except IOError as error :
        print(" Failed Operation " , error.strerror)
def read_order_file_to_dataframe():
    try:
        order_df = pd.DataFrame()
        with open(getenv('file_path') + 'orders.json.txt') as f:
            read_lines=f.readlines()
    #print(read_lines[0])
            for i in read_lines:
                d=json.loads(i)
                df=pd.DataFrame.from_dict(d,orient='columns')
                df['componentId']=df.index.values
                df.reset_index(drop=True, inplace=True)
                order_df=order_df.append(df,ignore_index=True)
                order_df['timestamp'] = order_df['timestamp'].astype('datetime64[ns]').dt.date
            return order_df
    except Exception as error :
        print(error)

def units_per_component(date):
    try:
        components_df= read_component_file_to_dataframe()
        order_df=read_order_file_to_dataframe()       
        result_df = pd.merge(order_df, components_df, on="componentId")
        final_df=result_df[result_df.timestamp.astype(str)==date].groupby(['colour'])['units'].sum().reset_index()
        print(final_df.to_string(index=False))
    except Exception as error :
        print(error)
       
        
if __name__ == '__main__':
    
    units_per_component(sys.argv[1])




       

