from pandas import Series
from nltk import RegexpTokenizer
import regex


def clean_text(inputDataset: Series) -> Series:
    print("Removing punctuation, numbers and links:")

    removeList = []
    tokenizer = RegexpTokenizer(r"\w+")

    for rowNum in range(inputDataset.count()):
        text = str(inputDataset[rowNum])
        if text != "":
            # Remove URLs from text
            # Credit: https://bobbyhadz.com/blog/python-remove-url-from-text
            text = regex.sub(pattern = r"http\S+", repl = "", string = text)
            
            # Remove '’', '…', and '-' characters from text
            text = regex.sub(pattern = r"[’…-]", repl = "", string = text)

            # Tokenize the text into words containing only 
            wordList = tokenizer.tokenize(text)

            # Rebuild our text with words that aren't numbers
            text = " ".join([word for word in wordList if not word.isnumeric()])

        # Hmm, the text has been obliterated or was empty this whole time...
        # Mark text to be removed from inputDataset
        if text == "":
            removeList.append(rowNum)

        inputDataset[rowNum] = text
        if rowNum % 10000 == 0 and rowNum != 0:
            print("Finished {0} lines".format(rowNum))

    inputDataset.drop(labels = removeList, inplace = True)
    inputDataset.reset_index(drop = True, inplace = True)

    print("Removed punctuation, numbers, links")
    return inputDataset