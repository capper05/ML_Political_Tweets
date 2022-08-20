import pandas as pd

df = pd.read_csv('ExtractedTweets.csv')

remove_list = []
for row_num in range(df.shape[0]):
    if df["Tweet"][row_num][0:4] == "RT @":
        remove_list.append(row_num)

df = df.drop(remove_list)
df = df.reset_index(drop=True)
print(df.shape)

print(df["Tweet"][36])
df.to_csv('cleanData.csv')