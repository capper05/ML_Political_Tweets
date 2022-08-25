from pandas import DataFrame

def tweets_to_lower_case(tweetDataSet: DataFrame) -> DataFrame:
    tweets = tweetDataSet.loc[:, 'Tweet']
    tweets = tweets.str.lower()

    tweetDataSet.update(tweets)
    return tweetDataSet