from pandas import DataFrame
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer


def split_vectorize(cleanData: DataFrame) -> tuple(DataFrame, DataFrame):
    tweets = cleanData["Tweet"].tolist()
    parties = cleanData["Party"].tolist()

    print("Splitting train and test data...")
    X_train, X_test, Y_train, Y_test = train_test_split(tweets, parties, test_size = 0.2, random_state = 653)

    vectorizer = TfidfVectorizer(min_df = 0.001, max_df = 0.95)
    print("Vectorizing train data...")
    X_train_vect = vectorizer.fit_transform(X_train).toarray()
    print("Vectorizing test data...")
    X_test_vect = vectorizer.transform(X_test).toarray()

    print("Creating train dataframe...")
    train_data = pd.DataFrame(X_train_vect, columns = vectorizer.get_feature_names_out())
    train_data["Party"] = Y_train
    print("Creating test dataframe...")
    test_data = pd.DataFrame(X_test_vect, columns = vectorizer.get_feature_names_out())
    test_data["Party"] = Y_test

    return train_data, test_data


def main():
    cleanData = pd.read_csv('cleanData.csv')

    train_data, test_data = split_vectorize(cleanData)

    print("Sending train data to csv...")
    train_data.to_csv('train_data.csv', chunksize = 1000)
    print("Updated 'train_data.csv'.")

    print("Sending test data to csv...")
    test_data.to_csv('test_data.csv', chunksize = 1000)
    print("Updated 'test_data.csv'.")


if __name__ == "__main__":
    main()