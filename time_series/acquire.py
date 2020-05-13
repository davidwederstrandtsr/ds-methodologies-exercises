import numpy as np
import pandas as pd
import requests

from os import path

# acquires the data from a url and the end point
def acquire_data(base_url, url_end):
    '''
    Returns a dataframe after acquiring json data from a url
    
    base_url: the main url of the website being accessed
    url_end: the targeted web page url name
    '''
    df = pd.DataFrame([])
    response = requests.get(base_url + f'/api/v1/{url_end}')
    data = response.json()
    
    for i in range(1, data['payload']['max_page']+1):
        response = requests.get(base_url + f'/api/v1/{url_end}?page={i}')
        data = response.json()
        i_list = data['payload'][url_end]
#         df = df.append(i_list)
        df = df.extend(i_list)
        
    return df

# 
def check_csv(base_url='', url_end=''):
    '''
    Returns a dataframe
    
    path.exists checks to see if the csv exists in the local storage
    
    - if the file is there:
        -reads the csv to a dataframe
    
    - if the file does not exist:
        - calls acquire_data()
        - writes csv files to local storage
        - reads csv to dataframe
    '''
    if path.exists(f'{url_end}.cvs'):
        df =pd.read_csv(f'{url_end}.cvs', index_col=0)
    else:
        df = acquire_data(base_url, url_end)
        df.to_csv(f'{url_end}.cvs')
        df =pd.read_csv(f'{url_end}.cvs', index_col=0)
        
    return df


def merge_sales(base_url, url1='', url2='', url3=''):
    '''
    Returns merged dataframe
    
    - calls check_csv():
        - datframes return:
            - items
            - stores
            - sales
            
    - merges sales and items dataframe:
        - the whole sales dataframe is eccientally copied to new dataframe
        - where sales.item and items.item_id match:
            - that items row is populated on the sales.item row
            * note: this is actually done on df not sales ~ sales is not changed
        - the same is performed on stores but with the new dataframe
        
    - new dataframe, we drop rows to prevent duplicates:
        - store
        - item
    '''
    items = check_csv(base_url, url1)
    stores = check_csv(base_url, url2)
    sales = check_csv(base_url, url3)
    df = sales.merge(items, left_on='item', right_on='item_id')
    df = df.merge(stores, left_on='store', right_on='store_id')
    df.drop(columns=(['store', 'item']), inplace=True)
    df.to_csv('time_sales.csv')
    
    return pd.read_csv('time_sales.csv', index_col=0)


def get_url_data(url):
    df = pd.read_csv(f'{url}')
    df.to_csv('german_power.csv')
    return pd.read_csv('german_power.csv', index_col=0)


    