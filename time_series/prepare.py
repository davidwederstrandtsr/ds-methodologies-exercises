import pandas as pd
import numpy as np
from os import path
import warnings

from datetime import timedelta, datetime

warnings.filterwarnings("ignore")


def get_store_data():
    return pd.read_csv('time_sales.csv', index_col=0)

def get_prep_data():
    return pd.read_csv('sales_date_converted.csv', index_col='sale_date', parse_dates=True)

def prep_store_data(df):
    if path.exists('store_data_converted.csv'):
        print('Acquired store_data_converted.csv from local storage')
    else:
        df = df.assign(sale_date=pd.to_datetime(df.sale_date)).sort_values('sale_date').set_index('sale_date')
        df.to_csv('store_data_converted.csv')
        print('Converting sale_date to datetime ...')
    print('Reading to dataframe ...')
     
    return pd.read_csv('store_data_converted.csv', index_col='sale_date', parse_dates=True)
        
        
        
        