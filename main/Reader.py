from typing import List, Any, Union
import xlrd
from main.Country import Country

class reader:
    data_temp = [0]
    str = input("Enter country one")
    doc = ("Country Data Spreadsheet")                  #opens the Excel file
    wb = xlrd.open_workbook(doc)
    sheet = wb.sheet_by_index(0)
    for i in sheet.nrows:
        if sheet.cell_value(0,i) == str:                    #collects data if it's the right country
            for j in sheet.ncols:
                data_temp.append(sheet.cell_value(i, j))

    c1 = Country(data_temp[0],data_temp[1],data_temp[2],data_temp[3],data_temp[4],data_temp[5],data_temp[6])        #creates first country
    data_temp.clear()           #clears the data

    str = input("Enter country two")
    doc = ("CountryData")
    wb = xlrd.open_workbook(doc)
    sheet = wb.sheet_by_index(0)
    for i in sheet.nrows:
        if sheet.cell_value(0, i) == str:                        #collects data for second country
            for j in sheet.ncols:
                data_temp.append(sheet.cell_value(i, j))

    c2 = Country(data_temp[0], data_temp[1], data_temp[2], data_temp[3], data_temp[4], data_temp[5], data_temp[6])           #creates second country
    data_temp.clear()       #clears data again