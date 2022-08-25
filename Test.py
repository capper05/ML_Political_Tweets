import pandas as pd

df = pd.read_csv('cleanData.csv')

print(df["Tweet"][88].encode('ascii'))