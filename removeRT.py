from pandas import Series
from pandas import isna

def remove_rt(inputDataset: Series) -> Series:
    print("Removing retweets:")

    removeList = []
    tweetList = inputDataset.to_list()

    for rowNum in range(inputDataset.count()):
        if str(tweetList[rowNum]).startswith("RT @"):
            removeList.append(rowNum)

        if isna(tweetList[rowNum]):
            removeList.append(rowNum)

        if rowNum % 10000 == 0 and rowNum != 0:
            print("\tFinished {0} lines".format(rowNum))

    inputDataset.drop(labels = removeList, inplace = True)
    inputDataset.reset_index(drop = True, inplace = True)

    print("Removed retweets!")
    return inputDataset