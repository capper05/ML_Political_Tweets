import pandas as pd
from nltk.stem.porter import *

def stem_words(df):
    print("Stemming words:")
    stemmer = PorterStemmer()
    remove_list = []
    for row_num in range(df.shape[0]):
        text = df["Tweet"][row_num]
        word_list = text.split()
        stemmed_list = [stemmer.stem(word) for word in word_list]
        new_text = " ".join(stemmed_list)
        df["Tweet"][row_num] = new_text
        if new_text == "":
            remove_list.append(row_num)
        if row_num % 10000 == 0 and row_num != 0:
            print("Finished {0} lines".format(row_num))
    df = df.drop(remove_list)
    df = df.reset_index(drop=True)
    print("Stemmed words")
    return df