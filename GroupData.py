import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math

products = pd.read_csv("course-files/WA_Sales_Products_2012-14.csv")


### PRZETWARZANIE DANYCH Z OBIOKTU GROUP
groups = products.groupby(by="Retailer country")

country_names = []

for country, data in groups:
    country_names.append(country)
    print(country, data['Revenue'].max() - data['Revenue'].min())

biggest = pd.DataFrame()
for country, data in groups:
    biggest = biggest.append(data.loc[data["Revenue"].idxmax()])
print(biggest)


# print(products.head())
# # print(products.info)
# print(products.describe())
# print(products["Retailer country"].value_counts())
# print(products["Retailer country"].nunique())
#
# countries = products['Retailer country'].unique()
# myOwnGroups = {}
# for country in countries:
#     myOwnSubDataFrame = products.where(products["Retailer country"] == country).dropna()
#     myOwnGroups[country] = myOwnSubDataFrame
#
# print(myOwnGroups)
#
# print(myOwnGroups["Belgium"].head())


# ### GROUPBY
# grouped_products = products.groupby(by="Retailer country")
# print(grouped_products.size())
# print(grouped_products.first())
# print(grouped_products.last())
#
# print(products.loc[grouped_products.groups['United States'][7]])
#
# print(grouped_products.get_group('Belgium').head())
#
# ### AGREGACJA
#
# print(grouped_products.mean().head())
# print(grouped_products.sum().head())
# print(grouped_products.count().head())
# print(grouped_products.min().head())
# print(grouped_products.max().head())
#
# print(grouped_products[['Revenue', 'Quantity']].mean())
#
# ### GRUPOWANIE a MULTIINDEX
# grouped_products = products.groupby(by=["Retailer country", "Year"])
# print(grouped_products.size())
# print(grouped_products.sum().head(10))
# print(grouped_products.get_group(('Australia', 2012)))
#
# ### AGG()
#
# print(grouped_products.agg(
#     {
#         "Revenue": ['sum', 'min', 'max'],
#         "Gross margin": ['sum', 'min', 'max'],
#         "Quantity": 'mean'
#     }
# ))


