import pandas as pd

df = pd.read_csv('ExtractedTweets.csv')

df.to_csv('cleanData.csv')