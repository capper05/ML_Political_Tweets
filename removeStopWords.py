from pandas import DataFrame, Series
from pandas import concat, read_csv, read_excel

import nltk
#nltk.download('punkt')
#nltk.download('stopwords')

from nltk.corpus import stopwords
from nltk import word_tokenize

def is_ascii(word):
    try:
        word.encode('ascii')
        return True
    except UnicodeEncodeError:
        return False

def remove_stop_words(inputData: DataFrame) -> DataFrame:
    print("Removing stopwords:")
    # Build Series with all words we want to remove from our Tweets
    wordsToRemove = read_excel('contractions.xlsx', dtype=str).squeeze('columns')
    wordsToRemove = concat([Series(stopwords.words('english')), wordsToRemove])

    # Obtain the column of the Twitter data with the tweets.
    tweetSeries = inputData.loc[:, 'Tweet']

    # Loop through list of tweets.
    for index, tweet in enumerate(tweetSeries.to_list()):
        # For each tweet, tokenize, remove stop words, and overwrite old tweet with filtered tweet in list.
        tokenizedTweet = word_tokenize(tweet)
        filteredTweet = [word for word in tokenizedTweet if not word in wordsToRemove.to_list()]
        tweetSeries[index] = ' '.join(filteredTweet)
        if index % 10000 == 0 and index != 0:
            print("Finished {0} lines".format(index))

    # Update the passed in Twitter data with the column of filtered tweets.
    inputData.update(tweetSeries)
    print("Removed stopwords")
    return inputData
