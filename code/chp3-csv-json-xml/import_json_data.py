import pandas as pd


json_data = pd.read_csv('../../data/chp3/data-text.csv')
for item in json_data.to_dict('record'):
    print(item)










