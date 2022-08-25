from pandas import DataFrame

def tweets_to_lower_case(tweetDataSet: DataFrame) -> DataFrame:
    print("Converting to lowercase:")
    tweets = tweetDataSet.loc[:, 'Tweet']
    tweets = tweets.str.lower()

    tweetDataSet.update(tweets)
    print("Converted to lowercase")
    return tweetDataSet