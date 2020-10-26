import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math


frame = pd.read_csv('./course-files/PublicTransitExpenses.csv',
                    usecols=['Agency', 'Reporter Type', 'Organization Type',
                             'Rail (Y/N)', 'Service Costs'],
                    low_memory=False) #
print(frame)

### PRZYGOTOWANIE DANYCH PO IMPORCIE
print(frame.info(memory_usage='deep'))

new = {'Reporter Type': 'ReporterType', 'Rail (Y/N)': 'isRail',
       'Service Costs': 'ServiceCosts'
       }
frame.rename(columns=new, inplace=True)
print(frame)
print(frame['ReporterType'].nunique())
print(frame['ReporterType'].value_counts())
frame['ReporterType'] = frame['ReporterType'].astype('category')
print(frame.info(memory_usage='deep'))


frame['Agency'] = frame['Agency'].astype('category')
print(frame.info(memory_usage='deep'))
print(frame['isRail'].head())

frame['isRail'].replace(('Y', 'N'), (True, False), inplace=True)
print(frame['isRail'].head())
print(frame.info(memory_usage='deep'))
frame['isRail'].fillna(False, inplace=True)

frame['isRail'] = frame['isRail'].astype('bool')
print(frame.info(memory_usage='deep'))
frame['ServiceCosts'] = frame['ServiceCosts'].str.replace('$', '')
frame['ServiceCosts']= frame['ServiceCosts'].astype('float')
print(frame.info(memory_usage='deep'))

frame['Agency'] = frame['Agency'].str.title().astype('category')
print(frame.info(memory_usage='deep'))


### OPERACJE NA KOLUMNACH TEKSTOWYCH
# contains = frame['Agency'].str.contains('Washington')
# endswith = frame['Agency'].str.endswith('Ferries')
# print(frame[contains & endswith])
# 
# frame.set_index('Agency', inplace=True)
# print(frame)
# frame.index = frame.index.str.strip().str.upper()
# print(frame)
# 
# frame[['ReporterTyp1', 'RepType2']] = frame['Reporter Type'].str.split(' ', expand=True)
# frame.drop(axis=1, columns=['Reporter Type'], inplace=True)
# print(frame)



# PRZEBUDOWA INDEKSU
# frame = pd.read_csv('./course-files/mammals.csv')
# print(frame.head())
# print(frame.set_index('name', inplace=True))
# # print(frame.reset_index())
# print(frame.loc['Cow'])
#
# frame.sort_index(inplace=True)
# print(frame)
# print(frame.loc['Cow'])
# print(frame['Cat': 'Donkey'])
# print(frame['A': 'F'])
## DODAWANIE I ODEJMOWANIE WIERSZY I KOLUMN
#
# frame.drop(axis=1, columns='awake', inplace=True)
# print(frame)
# ## axis = 0 to wiersze,
# frame.drop(axis=0, labels=[1,2,3], inplace=True)
# print(frame)
#
# frame.drop(5, inplace=True)
# print(frame)
#
# # frame.append({kolumna: dana}, ignore_index=True)
# # tak dla każdej kolumy
#
# subset = frame[0:6]
# frame = frame.append(subset)
#
# print(frame)

## Modyfikacja danych
# frame = pd.read_csv('./course-files/insurance.csv')
#
# lower25 = frame['Age'] == "<25"
# print(frame[lower25])
# print(frame.where(lower25).dropna())
#
# print(frame.loc[lower25, "Holders"] + 100)
# frame.loc[lower25, "Holders"] += 100
# print(frame)
# frame.loc[2, "Claims"] = frame.loc[2, "Claims"] - 1
# frame.loc[2, "Claims"] += 1
# print(frame)


## Zmiana nazwy
# frame = pd.read_csv('./course-files/mammals.csv', index_col='name')
# print(frame)
# print(frame.columns)
# frame.columns = ['name', 'bodyKG', 'brainKG']
# print(frame)
# NewColumnNames = {'bodyKG': 'body_kg', 'brainKG': 'brain_kg'}
# frame.rename(columns=NewColumnNames, inplace=True)
# print(frame)
#
# frame.rename(index={'Cow': 'LandCow'}, inplace=True)
# print(frame)
# cpyframe = frame.copy()
# cpyframe.loc['Artic fox', 'body'] = 5
# print(cpyframe)
# print(frame)
