from pandas import Series
from nltk.stem.porter import PorterStemmer

def stem_words(inputDataset: Series) -> Series:
    print("Stemming words:")

    stemmer = PorterStemmer()
    removeList = []

    # Loop through each string in inputDataset
    for rowNum in range(inputDataset.count()):
        text = str(inputDataset[rowNum])

        # If the string isn't empty, stem each word in the string
        if text != "":
            wordList = text.split()
            stemmedList = [stemmer.stem(word) for word in wordList]

            # Stemmed words are now joined together into a single string
            text = " ".join(stemmedList)
            inputDataset[rowNum] = text

        # If the string is empty, queue it up to be removed from inputDataset
        if text == "":
            removeList.append(rowNum)

        if rowNum % 10000 == 0 and rowNum != 0:
            print("Finished {0} lines".format(rowNum))

    inputDataset.drop(labels = removeList, inplace = True)
    inputDataset.reset_index(drop = True, inplace = True)

    print("Stemmed words")
    return inputDataset