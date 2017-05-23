"""
    This is a script to parse child labor and child marriage data.
    The excel file used in this script can be found here:
        http://www.unicef.org/sowc2014/numbers/
"""

import pandas as pd


sheet = pd.read_excel("../../data/chp4/SOWC 2014 Stat Tables_Table 9.xlsx",
                      sheetname="Table 9 ")

data = {}
for idx, row in sheet.iterrows():
    if idx < 14:
        continue
    country = row[0]
    data[country] = {
        'child_labor': {
            'total': [row[3], row[4]],
            'male': [row[5], row[6]],
            'female': [row[7], row[8]],
        },
        'child_marriage': {
            'married_by_15': [row[9], row[10]],
            'married_by_18': [row[11], row[12]],
        }
    }

    if country == "Zimbabwe":
        break

import pprint
pprint.pprint(data)
