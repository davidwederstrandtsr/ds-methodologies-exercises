# Throughout the exercises for Regression in Python lessons, you will use the following example scenario: 
# As a customer analyst, I want to know who has spent the most money with us over their lifetime. 
# I have monthly charges and tenure, so I think I will be able to use those two attributes as features 
# to estimate total_charges. I need to do this within an average of $5.00 per customer.

# The first step will be to acquire and prep the data. Do your work for this exercise in a file named wrangle.py.

# 1. Acquire customer_id, monthly_charges, tenure, and total_charges from telco_churn database 
#    for all customers with a 2 year contract. 
# 2. Walk through the steps above using your new dataframe. You may handle the missing 
#    values however you feel is appropriate.
# 3.End with a python file wrangle.py that contains the function, wrangle_telco(), 
#   that will acquire the data and return a dataframe cleaned with no missing values.

import pandas as pd
import numpy as np 
import env

def get_sql():
    return """
    select customer_id, tenure, monthly_charges, total_charges
    from customers
    where contract_type_id = 3;
    """
def get_url():
    return f'mysql+pymysql://{env.user}:{env.password}@{env.host}/telco_churn'

def wrangle_telco():
    df = pd.read_sql(get_sql(), get_url())
    df.tenure.replace(0, 1, inplace=True )
    df.total_charges = df.total_charges.str.strip()
    df = df[df.total_charges != ""]
    df.total_charges = df.total_charges.astype(float)
    return df




