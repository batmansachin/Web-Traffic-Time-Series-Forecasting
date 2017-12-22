import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)


train = pd.read_csv("../input/train_2.csv")
train = train.fillna(0.)
Windows = [3, 6, 9, 27, 81, 243, 729]


n = train.shape[1] - 1 #  550
Visits = np.zeros(train.shape[0])
for i, row in train.iterrows():
    M = []
    start = row[1:].nonzero()[0]
    if len(start) == 0:
        continue
    if n - start[0] < Windows[0]:
        Visits[i] = row.iloc[start[0]+1:].median()
        continue
    for W in Windows:
        if W > n-start[0]:
            break
        M.append(row.iloc[-W:].median())
    Visits[i] = np.median(M)

Visits[np.where(Visits < 1)] = 0.
train['Visits'] = Visits


test = pd.read_csv("../input/key_2.csv")
test['Page'] = test.Page.apply(lambda x: x[:-11])

test = test.merge(train[['Page','Visits']], on='Page', how='left')
test[['Id','Visits']].to_csv('sub.csv', index=False)