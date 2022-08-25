import pandas as pd
import nltk
import string

def clean_text(df):
    print("Removing punctuation, numbers and links:")
    remove_list = []
    tokenizer = nltk.RegexpTokenizer(r"\w+")
    for row_num in range(df.shape[0]):
        text = df["Tweet"][row_num]
        if "http" in text:
            text = text[:text.find("http")]

        text = text.replace("’","")
        text = text.replace("…","")
        text = text.replace("-","")
        #text = text.translate(str.maketrans('', '', string.punctuation)
        word_list = tokenizer.tokenize(text)

        new_text = " ".join([word for word in word_list if not word.isnumeric()])

        if new_text == "":
            remove_list.append(row_num)

        df["Tweet"][row_num] = new_text
        if row_num % 10000 == 0 and row_num != 0:
            print("Finished {0} lines".format(row_num))
    df = df.drop(remove_list)
    df = df.reset_index(drop=True)
    print("Removed punctuation, numbers, links")
    return df