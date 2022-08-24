import pandas as pd
df = pd.read_csv('ExtractedTweets.csv',encoding="utf-8",dtype=str)
print("Imported Tweet Data")

import removeRT
df = removeRT.remove_rt(df)
print("Removed retweets")

import cleanText
df = cleanText.clean_text(df)
print("removed punctuation, numbers, links")

# print(df["Tweet"][25])
df.to_csv('cleanData.csv')