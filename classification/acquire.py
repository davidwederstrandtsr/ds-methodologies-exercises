import pandas as pd
import numpy as np
import env

def get_titanic_sql():
     return '''
        select * 
        from `passengers`
    '''

def get_titanic_url():
    return f'mysql+pymysql://{env.user}:{env.password}@{env.host}/titanic_db'

def get_titanic_data():
    df = pd.read_sql(get_titanic_sql(), get_titanic_url())
    print('- CodeUp_db successfully accessed ...')
    print('- titanic_db SQL query successful ...')
    
    return df

def get_iris_sql():
         return '''
        select * 
        from `measurements`
        join `species` using (`species_id`)
    '''

def get_iris_url():
    return f'mysql+pymysql://{env.user}:{env.password}@{env.host}/iris_db'

def get_iris_data():
    df = pd.read_sql(get_iris_sql(), get_iris_url())
    print('- CodeUp_db successfully accessed ...')
    print('- iris_db SQL query successful ...')
    
    return df