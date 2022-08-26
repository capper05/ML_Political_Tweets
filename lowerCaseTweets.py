from pandas import Series

def tweets_to_lower_case(inputDataset: Series) -> Series:
    print("Converting to lowercase:")
    inputDataset = inputDataset.str.lower()

    print("Converted to lowercase")
    return inputDataset