import pandas as pd
import numpy as np

def custom_isnan(item):
    try:
        x = np.isnan(item)
        return True
    except:
        return False

def remove_rt(df):
    print("Removing retweets:")
    remove_list = []
    tweet_list = df["Tweet"].tolist()
    for row_num in range(df.shape[0]):
        if tweet_list[row_num][0:4] == "RT @":
            remove_list.append(row_num)
        if pd.isna(tweet_list[row_num]):
            remove_list.append(row_num)
            print(row_num)
        if row_num % 10000 == 0 and row_num != 0:
            print("Finished {0} lines".format(row_num))
    df = df.drop(remove_list)
    df = df.reset_index(drop=True)
    print("Removed retweets")
    return df
    #print(df.shape)

    #print(df["Tweet"][36])