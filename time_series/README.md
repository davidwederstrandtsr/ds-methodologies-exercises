# TIME-SERIES

## acquire.py
- acquire_data(base_url, url_end)
    - returns a dataframe after acquiring a json file from a url
        - base_url: the main url of a targeted website
        - url_end: the last element of the full url path

- check_csv(base_url, url_end)
    - returns a dataframe
        - check to see if a csv file exists
            - if present, creates dataframe from csv file
            - else
                - acquires data from url
                - creates csv file
                - creates dataframe from csv

- merge_sales(base_url, url1, url2, url3)
    - creates items, stores, and sales dataframes
    - merges dataframes on one dataframe
        - sales and items merged on
            - sales(item) ~ dropped
            - items(item_id)
        - new dataframe and stores merged on
            - stores(store) ~ dropped
            - df(store_id)
    - write df to csv
    - read and return csv

- get_url_data(url)
    - return dataframe acuired from web
        - url read from webpage
    