import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math

### MAP

team = pd.Series(
    data=[5, 3, 2, 4, 3],
    index=['Andy', 'Gas', 'Chris', 'Dirk', 'Ka']
)
notes = pd.Series(
    data=['C', 'B','A', 'A+', 'a++'],
    index=[1, 2, 3, 4 ,5]
)

print(team.map(notes))


# a = pd.read_csv("course-files/pokemon.csv", usecols=['Name'], squeeze=True)
#
# nIn = pd.read_csv("course-files/pokemon.csv", usecols=['Name', 'Type 2'], squeeze=True, index_col='Name')
#
#
# # def ReplaceType(oldType):
# #     if oldType=="Grass" or oldType=="Ground":
# #         return "Nature"
# #     return oldType
# print(nIn)
# # nIn.apply(lambda text: text.upper()) Dla wszystkich danych wywołaj funkcje

# new = nIn.apply(ReplaceType)

# print(nIn['Volcanion'])

### liczba każdej takiej samej wartości
# print(nIn.value_counts())
# print(new.value_counts())

# ind = ['A', 'B', 'C', 'D']
# val = ['Aust', 'Belg', 'Czechy', 'Dania']
# s = pd.Series(val, ind)

##REINDEX INTERSECTION
search = ['A', 'B', 'f']
# # print(s.loc[search]) Błąd
# print(s.reindex(search))
# print(s.loc[s.index.intersection(search)])
# print(s[1])
# #GET
# print(s.get('A'))
# print(s.get(0))
# print(s.get(8))
# #AT
# # print(s.at[1])
# print(s.at['A'])
# # print(s.at['Czechy'])
# #IAT
# # print(s.iat[[0,1]])
# print(s.iat[1])
# #LOC
# # print(s.loc[1])
# # print(s.loc['Czechy'])
# print(s.loc['A'])
# #ILOC



#### Sortowania i sprawdzanie czy jest w series

# print(a.sort_values())
# print(a.sort_values(ascending=False))
# print("-"*50)
# print(a.sort_values(inplace=True))
# print("-"*50)
# print(a.sort_index(inplace=True))
# print("-"*50)
# print('Abra' in a.values)
# print(-1 in a)
# print(2 in a.index)
# print(a[[1,5,7,12,5]])
# print()
# print()



### METODY PYTHONA NA OBIEKCIE SERIES
# print(a)
# print(type(a))
#
# print(len(a))
# print(a.head(10))
# print(sorted(a.head(10)))
# print(list(a.head()))
# print(dict(a.head()))
# print(min(a))
# print(max(a))
# print(a.name)



### PLOTS
# plt.plot([1,2,3,4])
# plt.ylabel('some numbers')
# # plt.show()
#
# plt.plot([1,2,3,4], [1, 4, 9, 16], 'ro')
# plt.ylabel('some numbers')
# # plt.show()
#
# t = np.arange(0., 5., 0.2)
# print(t)
#
# plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
# plt.ylabel('some numbers')
# # plt.show()
#
# ### SIN
# Min = 0
# Max = 4 * np.pi
#
# Step = 0.1
#
# x = np.arange(Min, Max, Step)
# y = np.sin(x)
#
# plt.plot(x, y)
# plt.xlabel('angle')
# plt.ylabel('sin - angle')
# # plt.show()
#
# #### DATA SERIES
#
# cities = [1, 2, 3, 4]
# ser = pd.Series(cities)
# print(ser)
# print(ser[0])
# print(ser > 2)
# print("-"*30)
#
#
# num = ser > 1
# num1 = ser % 2 == 1
#
# print(num)
# print(num1)
#
# print(ser.where(num & num1))

# print(ser.where(ser > 2, other=-1))
# print("-"*30)
# print(ser.where(ser > 2).dropna(inplace=True))
# print("-"*30)
# print(ser.filter(items=[1,2]))

# se




# print(ser.sort_values())
# print(ser[1])
# print(ser.is_monotonic_increasing)
# print(ser.index)
# print(ser.values)
# print(ser.sum())
# print("-"*30)
# print(ser.mean())
# print(ser.min())
# print(ser.product())
# print(ser.keys())
# print(ser.values)
# print(ser.to_json())
# print(ser.to_list())
# newSer = ser.add(10) # add to all
# print(newSer.values)
#
# curr = ['USD', 'PLN', 'PLN']
# country = ['Ameryka', 'Polska', 'Berlin']
#
# curser = pd.Series(country, curr)
# print(curser)
# print(curser['PLN'])
#

# primeNum = (2, 3, 4, 5, 6, 7,)
# ser = pd.Series(primeNum)
# print(ser)
#
# film = {'JAws': 1245, '1234': 5433}
# ser = pd.Series(film)
# print(ser)
