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
        df['month'] = df.index.month
        df['weekday'] = df.index.day_name()
        df = df.assign(sales_total = df.sale_amount * df.item_price)
        df = df.assign(sales_diff = df.sales_total.diff(periods=1))
        df = (df.astype({'sale_id': object, 'store_id': object, 'store_zipcode': object,
                         'item_id': object, 'item_upc12': object, 'item_upc14': object}))
        df.to_csv('store_data_converted.csv')
        print('Converting sale_date to datetime ...')
    print('Reading to dataframe ...')
     
    return pd.read_csv('store_data_converted.csv', index_col='sale_date', parse_dates=True)
        
        
        
        