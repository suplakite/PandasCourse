import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math


categories = pd.read_csv('course-files/northwind-mongo-master/categories1.csv',
                         )

products = pd.read_csv('course-files/northwind-mongo-master/products.csv',

                       )
suppliers = pd.read_csv('course-files/northwind-mongo-master/suppliers.csv',
                         usecols=['SupplierID', 'CompanyName', 'Country']
                         )
customers = pd.read_csv('course-files/northwind-mongo-master/customers.csv',
                        usecols=['CustomerID', 'CompanyName', 'Country']
                        )


print(len(suppliers))
print(len(customers))

### APPEND

df_appended = suppliers.append(customers, ignore_index=True) # Nowe Indeksy nie powtórzą się
print(len(df_appended))

print(df_appended.head(40))


suppliers2 = suppliers.copy()
customers2 = customers.copy()

suppliers2.rename({'SupplierID': 'CustomerID'}, axis='columns', inplace=True)
print(suppliers2.head())
print("-"*30)
df_appended2 = suppliers2.append(customers2, ignore_index=True) # Nowe Indeksy nie powtórzą się
print(df_appended2)

### CONCATENATE

concat = pd.concat(objs=[suppliers2, customers], ignore_index=True)
print(len(concat))
print(concat)


### JOIN
# products1 = pd.read_csv('course-files/northwind-mongo-master/products.csv',
#                        usecols=['ProductID', 'ProductName'], index_col='ProductID'
#                        )
#
# products2 = pd.read_csv('course-files/northwind-mongo-master/products.csv',
#                        usecols=['ProductID', 'UnitPrice', 'UnitsInStock'], index_col='ProductID'
#                        )
#
#
# print(products1.head())
# print(products2.head())
#
# joined = products1.join(products2, on="ProductID", lsuffix='lewa', rsuffix='prawa')
# print(joined)

categories1 = pd.read_csv('course-files/northwind-mongo-master/categories1.csv',
                         usecols=['CategoryID', 'CategoryName', 'Description']
                         )

products1 = pd.read_csv('course-files/northwind-mongo-master/products.csv',
                       usecols=['ProductID', 'ProductName', 'UnitPrice', 'CategoryID'], #index_col='ProductID'
                       )

categories1.set_index("CategoryID", inplace=True)


joined = products1.join(categories1, on='CategoryID') ### Można tylko po indeksie więc trzeba wyżej to zmienić na indeks

print(joined)



### MERGE

cat1 = pd.read_csv('course-files/northwind-mongo-master/categories_del_1.csv')
cat2 = pd.read_csv('course-files/northwind-mongo-master/categories_del_2.csv')
## how określa czy inner, outer join czy left czy right
merged = cat1.merge(cat2, on='CategoryID', suffixes=['_1', '_2'], how='outer', indicator=True)
print(merged)


filter = merged["_merge"] == "right_only"
print(merged[filter])
merged1 = cat1.merge(cat2, left_on="CategoryID", right_on='CategoryID')

## right_index/ left_index  ->   tak jak on i left_on np po left_on i index_right połącz
print(merged1)



## LACZENIE # I WIĘCEJ DATAFRAME



ccategories = pd.read_csv('course-files/northwind-mongo-master/categories1.csv',
                         usecols=['CategoryID', 'CategoryName', 'Description']
                         )

pproducts = pd.read_csv('course-files/northwind-mongo-master/products.csv',
                        usecols=['ProductID', 'ProductName', 'CategoryID', 'UnitPrice']
                       )

orders = pd.read_csv('course-files/northwind-mongo-master/order-details.csv')


merged_prod = pproducts.merge(ccategories, on="CategoryID")
merged_all = merged_prod.merge(orders, on="ProductID", suffixes=['_Prod', '_Order'])
print(merged_all.info())








