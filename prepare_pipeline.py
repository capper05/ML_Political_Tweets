import pandas as pd

def main():
    parsedTweetData = pd.read_csv(filepath_or_buffer = 'ExtractedTweets.csv', encoding = 'utf-8', dtype = str)
    print("Imported tweet data")

    tweetColumn = parsedTweetData.loc[:, 'Tweet']

    from removeRT import remove_rt
    tweetColumn = remove_rt(tweetColumn)

    from cleanText import clean_text
    tweetColumn = clean_text(tweetColumn)

    from lowerCaseTweets import tweets_to_lower_case
    tweetColumn = tweets_to_lower_case(tweetColumn)

    from removeStopWords import remove_stop_words
    tweetColumn = remove_stop_words(tweetColumn)

    from stem_words import stem_words
    tweetColumn = stem_words(tweetColumn)

    parsedTweetData.update(tweetColumn)
    parsedTweetData.to_csv('cleanData.csv', chunksize = 1000)
    print("Finished")

if __name__ == "__main__":
    main()