import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math

# print(frame)
# frame.set_index("Region", inplace=True)
frame = pd.read_csv(
    "./course-files/Canadian Railway Crossing Incidents.csv"
)


#### METADANE MULTIINDEKSU
frame.set_index("Region", inplace=True)
frame.sort_index(inplace=True)
print(frame.index)
frame.reset_index(inplace=True)
frame.set_index(["Region", "EventType"], inplace=True)
print(frame)

print(frame.index)
print(frame.index.get_level_values(1))
# print(frame.)
print(frame.index.names)
frame.index.set_name(["Areas", "Event"])

### STACK UNSTACK
# frame = pd.read_csv(
#     "./course-files/Canadian Railway Crossing Incidents.csv"
# )
# frame.set_index(["Region", "EventType"], inplace=True)
# frame.sort_index(inplace=True)
#
# print(frame.head(10))
# print(frame.stack()) ## Tak jakby 3 poziom indexu
# print(frame.stack().to_frame())

# print(frame.unstack())

### SWAPLEVEL
# print(frame.swaplevel().sort_index()) # zamiana indeksu

## Wyszukiwanie danych w multiindexie
#
# print(frame.loc[('Alberta', "Accidents")])
# print(frame.loc['Alberta'])
# # print(frame.loc['Accidents'])
# print('-'*30)
# print(frame.iloc[2])
# print(frame.loc[('Alberta', "Accidents")].loc['Public passive'])
# print(frame.loc[('Alberta', "Accidents"), 'Public passive'])
# print(len(frame))
# print(len(frame.transpose()))
# print(frame.transpose())

