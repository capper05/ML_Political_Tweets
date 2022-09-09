from pandas import Series
from pandas import concat, read_excel

import nltk
nltk.download('punkt')
nltk.download('stopwords')

from nltk.corpus import stopwords
from nltk import word_tokenize

def remove_stop_words(inputDataset: Series) -> Series:
    print("Removing stopwords:")
    # Build Series with all stop words we want to remove from our strings
    wordsToRemove = read_excel('contractions.xlsx', dtype=str).squeeze('columns')
    wordsToRemove = concat([Series(stopwords.words('english')), wordsToRemove])

    # Iterate through inputDataset which contains a list of strings
    for index, text in enumerate(inputDataset.to_list()):
        # For each string: Tokenize, remove stop words, and overwrite the old string with filtered string in inputDataset.
        tokenizedText = word_tokenize(text)
        filteredText = [word for word in tokenizedText if not word in wordsToRemove.to_list()]
        inputDataset[index] = ' '.join(filteredText)
        if index % 10000 == 0 and index != 0:
            print("Finished {0} lines".format(index))

    print("Removed stopwords")
    return inputDataset
