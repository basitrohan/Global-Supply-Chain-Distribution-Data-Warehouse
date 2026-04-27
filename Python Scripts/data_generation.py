import pandas as pd
from faker import Faker
import random

fake = Faker()

# generating product dimensions
products = []
categories = ['Electronics','Medical Supplies', 'Automotive', 'Textiles']
for i in range(1,501):
    products.append({
        'product_id' : i,
        'category' : random.choice(categories),
        'unit_cost' : round(random.uniform(10.0, 500.0), 2) 
    })

# generating location dimensions
locations = []
for i in range(1,101):
    locations.append({
        'location_id':i,
        'city' : fake.city(),
        'country' : fake.country(),
        'region' : random.choice(['North America', 'Europe', 'Asia', 'Middle East', 'Africa'])
    })

# generating shipments as fact
shipments = []
for i in range (1,15001):
    shipments.append({
        'shipment_id' : i,
        'product_id' : random.randint(1, 500),
        'location_id' : random.randint(1,100),
        'quantity': random.randint(1,50),
        'ship_date' : fake.date_between(start_date='-2y', end_date='today'),
        'delivery_date' : fake.date_between(start_date='today', end_date='+45d'),
        'shipping_cost' : round(random.uniform(100.0, 5000.0),2)  
    })

# generating supplier costs(excel)
supplier_data = []
for i in range(1,501):
    supplier_data.append({
        'product_id' : i,
        'supplier_name' : fake.company(),
        'lead_time_days' : random.randint(5,45),
        'negotiated_rate' : round(random.uniform(5.0,400.0),2)
    })

# generating quality inspections
inspections = []
for i in range(1,15501):
    inspections.append({
        'shipment_id' : i,
        'inspection_status' : random.choices(['Pass','Fail'], weights=[95, 5])[0],
        'defect_type': random.choice(['None', 'Packaging', 'Late Arrival', 'Damaged Item'])
    })

# saving csvs
pd.DataFrame(products).to_csv('products.csv',index=False)
pd.DataFrame(locations).to_csv('locations.csv',index=False)
pd.DataFrame(shipments).to_csv('shipments.csv',index=False)
pd.DataFrame(supplier_data).to_excel('supplier_data.xlsx', index= False)
pd.DataFrame(inspections).to_csv('inspections.csv', index=False)