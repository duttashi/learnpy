# objective: create a basic knn classifier
# script create date: 24/2/2020
# script last modified date:

# load required libraries
from sklearn.datasets import load_iris
import pandas as pd
# save data
iris = load_iris()
# coerce iris data to pandas dataframe so as to look at the data structure.
df = pd.DataFrame(iris.data, columns= iris.feature_names)
# look at the data structure
df.info()
# store feature matrix in "X"
X_train = iris.data
# store response varaible in y
y_test = iris.target
# print the shape of X and y
print(X_train.shape, y_test.shape)

# scikit-learn 4-step modeling pattern

# Step 1: Import the algorithm you plan to use
from sklearn.neighbors import KNeighborsClassifier

# Step 2: "Instantiate" the "estimator"
# "Estimator" is scikit-learn's term for model
# "Instantiate" means "make an instance of"
knn = KNeighborsClassifier(n_neighbors=1)
print(knn)

# Step 3: Fit the model with data (aka "model training")
#
# Model is learning the relationship between X and y
# Occurs in-place
train_model = knn.fit(X_train,y_test)
#print(train_model)

# Step 4: Predict the response for a new observation
#
# New observations are called "out-of-sample" data
# Uses the information it learned during the model training process
X_train_new = [[3, 5, 4, 2], [5, 4, 3, 2]]
test_model = knn.predict(X_train_new)
print(test_model)




