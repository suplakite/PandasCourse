import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math


# airports = pd.read_csv('course-files/mobile_internet_use_isoc_cimobi_frq.tsv', delimiter='\t')#, sep='\t'
# print(airports.head())
# new = airports['indic_is,ind_type,unit,time\geo'].str.split(',', expand=True)
# print(new)
#
# new.rename({0: 'unit', 1: 'tra_meas', 2: 'aiport', 3: 'year'}, axis=1, inplace=True)
# print(new)
#
# nn = new.join(airports)
# print(nn)



df_blood = pd.DataFrame({'Group': ['0', '0', 'A', 'A', 'B', 'B', 'AB', 'AB'],
                         'Rh': ['+', '-', '+', '+', '-', '-', '+', '-'],
                         'Population': [31, 6, 4, 46, 5, 4, 4, 2],
                         })


df_blood.to_csv('blood.csv', index=False)

blood = pd.read_csv('blood.csv')
print(blood)

print(blood.loc[:, "Population"] / 100)

read = pd.read_excel(
    './course-files/PC_Vehicles-in-use.xlsx',
    #sheet_name='Old Europe',
    sheet_name=[1, 2, 3], # NUMER LUB NAZWA ARKUSZA
)
print(read)
print(type(read))
print(read[1])


excelWriter = pd.ExcelWriter('cars.xlsx')
read[1].to_excel(excelWriter, index=False, sheet_name='Old')#, columns='')
excelWriter.save()