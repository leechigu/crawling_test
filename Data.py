import openpyxl as xl
import pandas as pd



temp = wb = pd.read_excel('seoul' + str(0) + '.xlsx')

count =0
dt = []
for i in range(1,55):
    wb = pd.read_excel('seoul' + str(i) + '.xlsx')
    temp = pd.concat([temp,wb],ignore_index=True)
    for j in range(0,100):
        dt.append(wb.loc[j])
        count+=1





temp.to_excel('seoulTotal.xlsx')
