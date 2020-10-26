import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math
# DATA SERIES
dS = pd.read_csv("./course-files/mcdonalds.csv",
                 usecols=['Item', 'Calories'],
                 index_col='Item',
                 squeeze=True
                 )


dF = pd.read_csv("./course-files/mcdonalds.csv",
                 usecols=['Item', 'Calories', 'Category', 'TotalFat', 'Serving Size', 'Protein'],
                 # index_col='Item',
                 )

### DUPLIKATY W DATA FRAME
print(dF['Calories'].is_unique) # czy sa tylko unikalne wartości
print(dF['Calories'].unique()) # unikalne wartości w DF
print(dF['Calories'].nunique()) # liczba unikalnych wartości w DF
print(dF['Calories'].duplicated(keep='first')) # pierwsze są false ale następny
# taki sam już true czyli duplikat,
# więc można wywalić te które mają
# true bo są duplikatami a orginaly zachowac
print(dF['Calories'].duplicated(keep='last')) # ostatnie mają False
print(dF['Calories'].duplicated(keep=False)) # Wszystkie co są kilka razy mają True
uniqueVal = dF['Calories'].duplicated(keep=False)
print(dF[~uniqueVal])  # tylko unique Categories

print(dF.drop_duplicates(subset=['Calories', 'Category'], keep=False)) # Jezeli kombinacja calori i categori jest unikalna to zostaw






### ISIN, ISNULL, NOTNULL, BETWEEN


# print(dF['Category'].isin(['Deserts', 'Beverages']))
# print(dF['Category'].notnull())
# print(dF['Category'].isnull())
# bet300_400 = dF['Calories'].between(300, 400)
# print(dF[bet300_400]['Calories'])

### WHERE I QUERY
# has400Cal = dF['Calories'] >= 400
#
# print(dF.where(has400Cal).dropna(how='all'))  ## Where nie spełnione zamienia na NaN
#
# print(dF.query('Category == "Desserts"'))
# print(dF.query('Category in ["Deserts", "Beverages"] and Calories < 200'))



# FILTROWANIE DANYCH
# print((dF['Calories'] >= 400).head())
#
# TotalCal = dF['Calories'] >= 400
#
# print(dF[TotalCal])
# print(dF[dF['Calories'] >= 400])
#
# isBreakFast = dF['Category'] == 'Breakfast'
# print(dF[~isBreakFast & TotalCal])  # ~ -> ! negacja


# ### RANKINGI
# print(dF)
# dF['CalRank'] = dF['Calories'].rank(ascending=False)
# print(dF.sort_values(by='Calories', ascending=False))
# print(dF.nlargest(3, columns='Calories'))
# print(dF.nsmallest(3, columns='Calories'))


### KONTROLA TYPÓW

# print(dF.dtypes)
# print(dF.info(memory_usage='deep'))
# dF.loc[2, 'Calories'] = np.NAN
# print(dF.info(memory_usage='deep'))
# # dF['Calories'].astype('int') Blad bo jest jakij not a number
# dF['Calories'].fillna(value=0, inplace=True)
# dF['Calories'] = dF['Calories'].astype('int')
# #
# print(dF.info(memory_usage='deep'))
#
#
# print(dF['Category'].value_counts())
# dF['Category'] = dF['Category'].astype('category')
# dF['Serving Size'] = dF['Serving Size'].astype('category')
# print(dF['Category'])   # W tej kolumnie powtarzają się kategorie i zamieniamy na category odchudza to pamięć
#
# print(dF.info(memory_usage='deep'))

## DROPNA   Usuwanie jezeli czegos brakuje
# dF.dropna(how='all')   Usuń jeżeli w wierszu how=all wszystkie dane są NaN
# dF.dropna(how='all', subset=["TotalFat"])   usun gdy w wierszu TotalFat jest Nan

# dF.dropna(axis='rows').head()   axis -> czy chpdzi o kolmnty czy o wiersze
#  czyli gdy rows w usuwaniu to usunie wiersz jezeli jest NaN
#  else usunie cala kolumne jezeli chociaz jeden jest NaN

# dF.dropna(axis='rows').head()   to zwraca nowy obiekt
# dF.dropna(axis='rows', inplace=True).head() gdy inplace True to operacje wykonane sa na tym obiekcie

## FILNA Uzypełnianie brakujących danych

# dF.fillna(value=0) uzupełnij NaN 0 można wstawic w value dziennik
# {Category: UNKNOWN, TotalFat: 0}

# df['Category'].fillna(value='UNKNOWN', inplace=True)
# df['Category'].fillna(value='UNKNOWN', inplace=True, method='ffill') # sokupiuj poprzednią wartość do NaN
# df['Category'].fillna(value='UNKNOWN', inplace=True, method='') # sokupiuj poprzednią wartość do NaN



### SORTOWANIE

# print(dF.sort_values(by='Category', ascending=False))
# print(dF.sort_values(by=['Category', 'Item'], ascending=[False, True]))
# # print(dF.sort_index(ascending=True))


####
# print(dF)
# print(dF.head())
# print(dF.tail())
# print(dF.count())
# print(len(dF))
# print(dF.index)
# print(dF.columns)
# print(dF.values)
# print(dF.info())
# print(dF.count())
# print(dF.value_counts())
# print(dF['Category'].value_counts())
# print(dF.sample(n=3))
#
#
# ### ATRYBUT ROBI SIE NAZWA KOLUMNY
# print(dF.Calories)
# print(type(dF.Calories))
# print(dF.Calories.mean())
# print(dF.Calories.median())
# print(dF.Calories.std())
# print(dF.Calories.max())
# print(dF.Calories.idxmax())
#
# print(dF["Calories"])
#
# s = dF["Category"][242]
# print(s)
# # print(s[242])
#
# print(dF.loc[2, "Item"])
#
# # print(type(dF))
#
# print(dF[['Item', 'Calories']])
#
# print(dF.TotalFat.head())
# print(dF['TotalFat'].head())
# dF['TotalFats'] = 0
# print(dF['TotalFats'])
# SugarandFat = dF.Sugars + dF.TotalFat
# # dF['SugarandFat'] = SugarandFat
# # print(dF['SugarandFat'])
# dF.insert(loc=2, column="SPF", value=SugarandFat)
# print(dF)
# del dF['SPF']
# print(dF)
# print(dF.drop(columns=["Sugars"]))
