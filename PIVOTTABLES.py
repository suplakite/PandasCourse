import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math

frame = pd.read_csv(
    "./course-files/WA_Sales_Products_2012-14.csv"
)
print(frame)

pivot = frame.pivot_table(index="Retailer country", columns=["Year", "Quarter"], values="Revenue")
print(pivot)


pivot3 = frame.pivot_table(
    index="Retailer country", columns="Year",
    values="Gross margin", aggfunc=["min", 'max']
)
print(pivot3)
print(pivot3.columns)
print(pivot3.swaplevel(axis='columns').sort_index(axis='columns'))


### MELT   pivot to data frame
pivot2 = frame.pivot_table(
    index="Retailer country",
    columns='Year',
    values="Revenue",
    aggfunc='sum'
)

print(pivot2)

pivotyt = pivot2.reset_index()

pivotyt = pivotyt.fillna(0)
print(pivot2)

pivotw2DF = pivotyt.melt(
    id_vars="Retailer country",
    value_name="RevenueSum",
    var_name="YearOfTransaction",
    value_vars=[2013, 2014]
)
print(pivotw2DF)
unpvt = pivot2.unstack().to_frame().swaplevel().head()
unpvt.columns = ['RevenueSum']
print(unpvt)