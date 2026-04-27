import pandas as pd
from sqlalchemy import create_engine

# connection setup
engine = create_engine('user_database_address')

try:
    #loading the 3 core tables
    print("loading shipments...")
    df_shipments = pd.read_csv(r'D:\Jupyter_files\shipments.csv')
    df_shipments.to_sql('shipments', engine, if_exists='replace', index=False)

    print("loading products...")
    df_products = pd.read_csv(r'D:\Jupyter_files\products.csv')
    df_products.to_sql('products', engine, if_exists='replace',index=False)

    print("loading locations...")
    df_locations = pd.read_csv(r'D:\Jupyter_files\locations.csv')
    df_locations.to_sql('locations', engine, if_exists='replace',index=False)

except Exception as e:
    print(f"Error:{e}")