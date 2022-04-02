import openpyxl
import pandas as pd


gu_dongs = []

def readExcel() :
    wb = openpyxl.load_workbook('다방크롤링/서울시 자치동 정보.xlsx')
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
print(gu_dongs)
