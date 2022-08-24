import pandas as pd
import nltk
import string

def clean_text(df):
    tokenizer = nltk.RegexpTokenizer(r"\w+")
    for row_num in range(df.shape[0]):
        text = df["Tweet"][row_num]
        if "http" in text:
            text = text[:text.find("http")]

        text = text.replace("’","")
        text = text.replace("…","")
        #text = text.translate(str.maketrans('', '', string.punctuation))
        word_list = tokenizer.tokenize(text)

        df["Tweet"][row_num] = " ".join([word for word in word_list if not word.isnumeric()])

    return df