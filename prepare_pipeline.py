import pandas as pd
df = pd.read_csv('ExtractedTweets.csv',encoding="utf-8",dtype=str)
print("Imported tweet data")

import removeRT
df = removeRT.remove_rt(df)
print("Removed retweets")

import cleanText
df = cleanText.clean_text(df)
print("Removed punctuation, numbers, links")

import lowerCaseTweets
df = lowerCaseTweets.tweets_to_lower_case(df)
print("Converted to lowercase")

# print(df["Tweet"][25])
df.to_csv('cleanData.csv')