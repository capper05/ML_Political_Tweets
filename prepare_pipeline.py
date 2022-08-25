import pandas as pd
import numpy as np
df = pd.read_csv('ExtractedTweets.csv',encoding="utf-8",dtype=str)
print("Imported tweet data")

import removeRT
df = removeRT.remove_rt(df)

import cleanText
df = cleanText.clean_text(df)

import lowerCaseTweets
df = lowerCaseTweets.tweets_to_lower_case(df)

import removeStopWords
df = removeStopWords.remove_stop_words(df)

import stem_words
df = stem_words.stem_words(df)

for row_num in range(df.shape[0]):
    if pd.isna(df["Tweet"].tolist()[row_num]):
        print(row_num)

# print(df["Tweet"][25])
df.to_csv('cleanData.csv')
print("Finished")