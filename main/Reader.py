from openpyxl import load_workbook
import numpy as np
from main import Country


class Reader:
    countries = np.zeros((10,10))
    str = input("Enter country one\n")
    wb = load_workbook('CountryData.xlsx')                  #opens the Excel file
    source = wb.active
    ws = wb.copy_worksheet(source)

    for i in range(2,11):
        country = ws.cell(row=i, column=1)
        if(country.value == str):
            a = ws.cell(row = i, column = 2).value
            b = ws.cell(row=i, column=3).value
            c = ws.cell(row=i, column=4).value
            d = ws.cell(row=i, column=5).value
            e = ws.cell(row=i, column=6).value
            f = ws.cell(row=i, column=7).value
            g = ws.cell(row=i, column=8).value
            c1 = Country.Country(a,b,c,d,e,f,g)

    str = input("Enter country two\n")
    for i in range(2,11):
        country = ws.cell(row=i, column=1)
        if(country.value == str):
            a =  ws.cell(row = i, column = 2).value
            b= ws.cell(row=i, column=3).value
            c= ws.cell(row=i, column=4).value
            d= ws.cell(row=i, column=5).value
            e= ws.cell(row=i, column=6).value
            f= ws.cell(row=i, column=7).value
            g=ws.cell(row=i, column=8).value
            c2 = Country.Country(a,b,c,d,e,f,g)


    print(c1.ID_TAG)
    print(c2.ID_TAG)