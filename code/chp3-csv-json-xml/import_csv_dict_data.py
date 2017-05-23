import pandas as pd


csvfile = pd.read_csv('../../data/chp3/data-text.csv')
for row in csvfile.to_dict('record'):
    print(row)
