import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

import os
import csv
with open('Scraped-Data/df_pivoted.csv','r') as f:
    reader = csv.reader(f,delimiter=',')
    i = next(reader)
    rest = [row for row in reader]
column_headings = i

with open('Scraped-Data/df_pivoted.csv','r') as f:
    df_pivoted=pd.read_csv(f,delimiter=',')
	
cols=df_pivoted.columns
cols = cols[1:]
df_pivoted = df_pivoted.groupby('Source').sum()
df_pivoted = df_pivoted.reset_index()
df_pivoted[:5]

cols = cols[1:]
x = df_pivoted[cols]
y = df_pivoted['Source']
#print (x)

from sklearn.tree import DecisionTreeClassifier
print ("DecisionTree")
dt = DecisionTreeClassifier()
clf_dt=dt.fit(x,y)
#print ("Acurracy: ", clf_dt.score(x,y))

data = pd.read_csv("Manual-Data/Training.csv")
data.head()
data.columns
len(data['prognosis'].unique())
df = pd.DataFrame(data)
df.head()

cols = df.columns
cols = cols[:-1]
x = df[cols]
y = df['prognosis']

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=42)
mnb = MultinomialNB()
mnb = mnb.fit(x_train, y_train)
mnb.score(x_test, y_test)

from sklearn import model_selection
print ("cross result========")
scores = model_selection.cross_val_score(mnb, x_test, y_test, cv=5)
#print (scores)
#print (scores.mean())

test_data = pd.read_csv("Manual-Data/Testing.csv")
test_data.head()
testx = test_data[cols]
testy = test_data['prognosis']
mnb.score(testx, testy)

def prediction(sym1,sym2,sym3):
    from sklearn.tree import DecisionTreeClassifier
    from sklearn.model_selection import train_test_split
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=42)
    #print ("DecisionTree")
    dt = DecisionTreeClassifier()
    clf_dt=dt.fit(x_train,y_train)
	#print ("Acurracy: ", clf_dt.score(x_test,y_test))
    from sklearn import model_selection
    #print ("cross result========")
    scores =model_selection.cross_val_score(dt, x_test, y_test, cv=6)
	#print (scores)
	#print (scores.mean())
	#print ("Acurracy on the actual test data: ", clf_dt.score(testx,testy))
    import numpy as np
    import matplotlib.pyplot as plt
    importances = dt.feature_importances_
    indices = np.argsort(importances)[::-1]
    feature_importances = pd.DataFrame(dt.feature_importances_,index = x_train.columns,columns=['importance']).sort_values('importance',ascending=False)
    print(feature_importances)
    features=cols
    feature_dict = {}
    for i,f in enumerate(features):
        feature_dict[f] = i
    sample_x = [0]*len(features)
    len(sample_x)
    for sym in range(1,4):
        #name = input("enter your symptoms  ")
        if sym==1:
            key=feature_dict[sym1]
            for i,f in enumerate(features):
                feature_dict[f] = i
                if i==key:
                    sample_x[i] = i/key
        if sym==2:
            key=feature_dict[sym2]
            for i,f in enumerate(features):
                feature_dict[f] = i
                if i==key:
                    sample_x[i] = i/key
        if sym==3:
            key=feature_dict[sym3]
            for i,f in enumerate(features):
                feature_dict[f] = i
                if i==key:
                    sample_x[i] = i/key
    #print(sample_x)
    len(sample_x)
    sample_x = np.array(sample_x).reshape(1,len(sample_x))
    return dt.predict(sample_x)

