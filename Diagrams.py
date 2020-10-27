import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math



bar = pd.read_csv('course-files/weather_barcelona.csv', index_col='Date')
rom = pd.read_csv('course-files/weather_rome.csv', index_col='Date')
ams = pd.read_csv('course-files/weather_amsterdam.csv', index_col='Date')




temp_max = pd.DataFrame(index = bar.index)

temp_max['Barcelona'] = bar["TempMax"]
temp_max['Amsterdame'] = ams["TempMax"]
temp_max['Rome'] = rom["TempMax"]




def GradeDay(row):
    if(row['TempMax'] >= row['AvgTempMax']):
        return 'Plus'
    return 'Minus'

rom['GradeDat'] = rom.apply(GradeDay, axis=1)
ams['GradeDat'] = ams.apply(GradeDay, axis=1)
bar['GradeDat'] = bar.apply(GradeDay, axis=1)

print(rom.head())
print(rom['GradeDat'].value_counts())

citeis3 = pd.DataFrame(index=['Minus', 'Plus'])
citeis3['Barcelona'] = bar['GradeDat'].value_counts()
citeis3['Rome'] = rom['GradeDat'].value_counts()
citeis3['Amsterdame'] = ams['GradeDat'].value_counts()

print(citeis3)

#### WYKRESY KOLOWE
# citeis3['Barcelona'].plot(kind='pie', figsize=(8,8))
# plt.show()

# citeis3.plot(kind='pie', figsize=(8,8),
#              subplots=True, colors=['b', 'g'],
#              labels=['colder', 'warmer'], autopct='%.0f%%',
#              fontsize=16, textprops=dict(color='w'),
#              layout=(2,2),
#              explode=(0.05, 0)
#              )
# plt.show()


### SLUPKOWY

# citeis3.plot(kind='barh', stacked=True)
# citeis3.plot(kind='barh')
# plt.show()

### PUDELKOWY/SKRZYNKOWY

# temp_max.plot(kind='box')
# plt.show()


### HISTOGRAM
# bar['TempMax'].plot(kind='hist', bins = bar['TempMax'].nunique())
# plt.show()

autos = pd.read_csv('course-files/autos.csv', encoding='latin-1')

def filter(name):
    import re
    regex = re.compile(name, re.IGNORECASE)
    f1 = autos['name'].apply(lambda x: bool(regex.search(x)))
    f2 = autos['price'] < 12000
    f3 = autos['yearOfRegistration']>=1990
    return autos[f1 & f2 & f3]


tc = filter('.*toyota.*corolla.*')
audi = filter('.*Audi.*a4.*')

### SCATTER
# ax = audi.plot.scatter(x='yearOfRegistration', y='price', color='Blue', label='Audi')
# tc.plot.scatter(x='yearOfRegistration', y='price', color='Green', label='Toyota', ax=ax)
# plt.show()


### HEXBIN

# tc.plot.hexbin(x='yearOfRegistration', y='price', gridsize=20,  label='Toyota')
# plt.show()
# audi.plot.hexbin(x='yearOfRegistration', y='price', gridsize=20,  label='Audi')
# plt.show()

tc_counts = tc['yearOfRegistration'].value_counts().sort_index()
print(tc_counts)
audi_counts = audi['yearOfRegistration'].value_counts().sort_index()
print(tc_counts)

car_counts = pd.DataFrame(index = tc_counts.index.append(audi_counts.index).unique())
car_counts["Toyota"] = tc_counts
car_counts["Audi"] = audi_counts
print(car_counts)
car_counts.fillna(0, inplace=True)
car_counts.sort_index(inplace=True)
car_counts.plot()
plt.show()

### AREA
car_counts.plot(kind="area")
plt.show()


#
# print(temp_max.head())
#
# # temp_max.plot(figsize=(15, 5), subplots=True, use_index=False, legend=False)
# # temp_max.plot(figsize=(15, 5), subplots=True, title='Max temp in cities')
# # temp_max.plot(figsize=(15, 5), logy=True)
# # temp_max[:7].plot(figsize=(15, 8), xticks=(range(14)), rot=45)
# temp_max[:7].plot(figsize=(15, 8), table=True)
# plt.show()
# # temp_max.plot(figsize=(15, 5), )


### PLOT
# print(bar.head())
#
# print(type(bar))

# bar.plot(color=['b', 'g', 'r', 'm', 'k'])
# # bar.plot(colormap='gnuplot')
# print(plt.style.available)
#
# bar.plot()
# plt.style.use('fast')
# plt.show()

# bar[['TempMax', 'TempMin']].plot()
# plt.show()


