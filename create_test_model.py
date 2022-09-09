from random import Random
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
import pandas as pd

print("Preparing training data")
train_data = pd.read_csv('train_data.csv',encoding="utf-8",index_col=0)
train_answers = train_data["Party"].tolist()
train_data = train_data.drop(["Party"],axis=1).values.tolist()

print("Preparing testing data")
test_data = pd.read_csv('test_data.csv',encoding="utf-8",index_col=0)
test_answers = test_data["Party"].tolist()
test_data = test_data.drop(["Party"],axis=1).values.tolist()

print("Training model")
lg = LogisticRegression(C=5, max_iter = 1000).fit(train_data,train_answers)
#lg = RandomForestClassifier(max_depth=5).fit(train_data,train_answers)

print("Testing model")
prob_array = lg.predict_proba(test_data)

print("Creating dataframe")
prob_frame = pd.DataFrame(prob_array)
prob_frame.columns = lg.classes_
prob_frame["Party"] = test_answers

bool_list = []
for i in range(0,len(prob_frame["Party"])):
    party = "Democrat"
    if prob_frame["Democrat"][i] < prob_frame["Republican"][i]:
        party = "Republican"
    if party == test_answers[i]:
        bool_list.append(True)
    else:
        bool_list.append(False)

prob_frame["Correct"] = bool_list

print("Sending results to results.csv...")
prob_frame.to_csv('results.csv',chunksize=1000)