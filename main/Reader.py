from openpyxl import load_workbook
import numpy as np
from main import Country


class Reader:
    countries = np.zeros((10,10))
    wb = load_workbook('CountryData.xlsx')                  #opens the Excel file
    source = wb.active
    ws = wb.copy_worksheet(source)

    def c1Init(self):
        ws = Reader.wb.copy_worksheet(Reader.source)
        c1 = Country.Country()
        str = input("Enter country one\n")
        for i in range(2, 11):
            country = ws.cell(row=i, column=1)
            if (country.value == str):
                c1.ID_TAG = ws.cell(row=i, column=2).value
                c1.GDP = ws.cell(row=i, column=3).value
                c1.ARMY_ASSETS = ws.cell(row=i, column=4).value
                c1.NAVY_ASSETS = ws.cell(row=i, column=5).value
                c1.AIR_FORCE_ASSETS = ws.cell(row=i, column=6).value
                c1.MANPOWER = ws.cell(row=i, column=7).value
                c1.NUCLEAR_CAPABILITIES = ws.cell(row=i, column=8).value
        return c1

    def c2Init(self):
        ws = Reader.wb.copy_worksheet(Reader.source)
        c2 = Country.Country()
        str = input("Enter country two\n")
        for i in range(2, 11):
            country = ws.cell(row=i, column=1)
            if (country.value == str):
                c2.ID_TAG = ws.cell(row=i, column=2).value
                c2.GDP = ws.cell(row=i, column=3).value
                c2.ARMY_ASSETS = ws.cell(row=i, column=4).value
                c2.NAVY_ASSETS = ws.cell(row=i, column=5).value
                c2.AIR_FORCE_ASSETS = ws.cell(row=i, column=6).value
                c2.MANPOWER = ws.cell(row=i, column=7).value
                c2.NUCLEAR_CAPABILITIES = ws.cell(row=i, column=8).value
        return c2
