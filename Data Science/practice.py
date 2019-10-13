# linear algebra
import numpy as np
# data processing
import pandas as pd
# Algorithms
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import cross_validate
from sklearn.model_selection import train_test_split

test_set = pd.read_csv('test.csv')
train_set = pd.read_csv('train.csv')

# Data Processing. Converting and droping all the columns we do not need
train_set = train_set.drop(['PassengerId'], axis = 1)

data = [train_set, test_set]
genders = {'male':0, 'female':1}

for dataset in data:
    mean = train_set["Age"].mean()
    mean2 = test_set["Age"].mean()
    # number of null values
    is_null = dataset["Age"].isnull().sum()
    # compute random numbers between the mean, mean2 and is_null
    rand_age = np.random.randint(mean - mean2, mean + mean2, size = is_null)
    # fill NaN values in Age column with random values generated
    age_slice = dataset["Age"].copy()
    age_slice[np.isnan(age_slice)] = rand_age
    dataset["Age"] = age_slice
    # Age type is an int
    dataset["Age"] = train_set["Age"].astype(int)
    dataset['Embarked'] = dataset['Embarked'].fillna('S')
    # Fare null values will be 0
    dataset['Fare'] = dataset['Fare'].fillna(0)
    dataset['Fare'] = dataset['Fare'].astype(int)
    # Males = 0 Females = 1
    dataset['Sex'] = dataset['Sex'].map(genders)

train_set['Age'].isnull().sum()

# Droping all columns we no not need in test and train datasets
train_set = train_set.drop(['Ticket'], axis = 1)
test_set = test_set.drop(['Ticket'], axis = 1)
train_set = train_set.drop(['Cabin'], axis = 1)
test_set = test_set.drop(['Cabin'], axis = 1)
train_set = train_set.drop(['Embarked'], axis = 1)
test_set = test_set.drop(['Embarked'], axis = 1)
train_set = train_set.drop(['Name'], axis = 1)
test_set = test_set.drop(['Name'], axis = 1)

train_X = train_set.drop("Survived", axis = 1)
train_Y = train_set['Survived']
test_X = test_set.drop("PassengerId", axis = 1)

X_train, X_test, Y_train, Y_test = train_test_split(train_X, train_Y, test_size=0.2)

d_tree = DecisionTreeClassifier(max_depth=10)
d_tree.fit(train_X, train_Y)
score = d_tree.score(X_test, Y_test)
print(round(score*100))
#
'''
prediction = d_tree.predict(test_X)
print(prediction)
accurarcy = round(d_tree.score(train_X, train_Y)*100)
print(accurarcy)
'''
