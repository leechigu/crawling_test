import openpyxl
import pandas as pd


gu_dongs = []

def readExcel() :
    wb = openpyxl.load_workbook('서울시 자치동 정보.xlsx')
    dong = pd.read_excel('서울시 자치동 정보.xlsx',usecols=[0,1,2])

    length  = len(dong.자치구_명칭)
    gus = []
    dongs = []
    for i in dong.자치구_명칭 :
        gus.append(i)
    for i in dong.행정동_명칭 :
        dongs.append(i)
    for i in range(length) :
        gu_dongs.append(gus[i]+" "+dongs[i])

readExcel()

count = 0
dt = []
temp = wb = pd.read_excel('엑셀/'+gu_dongs[0]+'.xlsx')
for gu_dong in gu_dongs :
    print(count)
    if(count ==0):
        count+=1
        continue;
    if (gu_dong == '송파구 장지동'):
        continue;
    elif (gu_dong == '용산구 남영동'):
        continue;
    elif (gu_dong == '종로구 청운효자동'):
        continue;
    elif (gu_dong == '종로구 종로5가'):
        continue;
    elif (gu_dong == '종로구 종로4가'):
        continue;
    elif (gu_dong == '종로구 종로3가'):
        continue;
    elif (gu_dong == '종로구 종로2가'):
        continue;
    elif (gu_dong == '종로구 종로1가'):
        continue;
    elif (gu_dong == '종로구 교남동'):
        continue;

    wb = pd.read_excel('엑셀/'+gu_dong+'.xlsx')
    temp = pd.concat([temp,wb],ignore_index=True)

    count+=1

temp.to_excel('다방ALL.xlsx')