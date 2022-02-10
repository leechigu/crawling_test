import csv

import pandas as pd



wb =pd.read_excel('seoulTotal.xlsx',engine='openpyxl')

temp =[]
for i in wb['API']:
    ar = i.split('\n')
    if(len(ar)==1):
        i=ar[0]
    else:
        i=ar[1]
    print(i)
    temp.append(i)

wb['API'] = temp
wb.to_excel('plz.xlsx',index=False)








