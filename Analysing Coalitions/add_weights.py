import pandas as pd
import numpy as np

df = pd.read_csv('small-data.csv', header=None)
df_tot = pd.read_csv('signed-unsigned-data.csv')

countries_dict = {1: "Ukraine", 
                  2: "United-States",
                  3: "Philippines",
                  4: "Chile",
                  5: "Canada",
                  6: "United-Kingdom",
                  7: "France",
                  8: "Germany",
                  9: "Spain",
                  10: "Italy",
                  11: "Japan",
                  12: "South-Korea",
                  13: "Australia",
                  14: "Jamaica",
                  15: "Libya",
                  16: "Russia",
                  17: "China",
                  18: "Vietnam",
                  19: "Iran",
                  20: "North-Korea",
                  21: "India",
                  22: "Brazil",
                  23: "Mexico",
                  24: "Pakistan",
                  25: "Singapore",
                  26: "South-Africa",
                  27: "Egypt",
                  28: "Malaysia",
                  29: "Saudi-Arabia",
                  30: "United-Arab-Emirates"}

df.replace(countries_dict, inplace=True)
df['weight'] = pd.Series()

for i in range(len(df)):
    source = df[0][i]
    target = df[1][i]
    weight = df_tot[(np.array(df_tot['Source'])==source) & (np.array(df_tot['Target'])==target)]['weight']
    df['weight'][i] = weight

df.columns = ['source', 'target', 'sign', 'weight']
df.to_csv('small-data-weighted.csv', index=False)