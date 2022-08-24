import pandas as pd
import removeRT


df = pd.read_csv('ExtractedTweets.csv')

df = removeRT.removeRT(df)

df.to_csv('cleanData.csv')