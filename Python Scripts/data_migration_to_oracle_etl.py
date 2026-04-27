import pandas as pd
from sqlalchemy import create_engine, Numeric

# creating connections 
pg_eng = create_engine('user_postgres_address')
ora_eng = create_engine('user_oracle_db_address')

# defining everything in one list
tasks = [
    ('shipments','stg_shipments','db'),
    ('products','stg_products','db'),
    ('locations','stg_locations','db'),
    ('inspections.csv','stg_inspections','csv'),
    ('supplier_data.xlsx','stg_supplier_data','xlsx')
]

for source, target, kind in tasks:
    print(f"...Migrating{source}...")

    if kind == 'db': 
        df = pd.read_sql(f'SELECT*FROM {source}',pg_eng)
    elif kind == 'csv': 
        df = pd.read_csv(source)
    elif kind == 'xlsx': 
        df = pd.read_excel(source)

    float_cols = df.select_dtypes(include=['float']).columns
    ora_dtypes = {col: Numeric for col in float_cols}

    df.to_sql(target, ora_eng, if_exists='replace', index=False, dtype=ora_dtypes)
    print(f"loaded{len(df)} rows into {target}")

print("...Task Completed Successfully...")