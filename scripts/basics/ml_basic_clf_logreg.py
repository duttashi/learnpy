# objective: create a basic logistic regression classifier
# script create date: 24/Feb/2020
# important points to remember
## logistic regression classifier accepts a categorical response variable. Also the input data should be ceneterd and scaled
## otherwise there is a warning.
# script create date: 24/2/2020
# script last modified date:

# load required libraries
from sklearn.datasets import load_iris
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn import preprocessing
from sklearn import utils

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

# print the data type of response variable
#print(utils.multiclass.type_of_target(y_test))

# scale the data
X_train_scaled = preprocessing.scale(X_train)
y_test_scaled = preprocessing.scale(y_test)
# print("y_test_scaled: ", y_test_scaled) # will print the original float values

# Encode the response variable to categorical
label_enc = preprocessing.LabelEncoder()
y_test_scaled_encoded = label_enc.fit_transform(y_test_scaled)
#print("y_test_scaled_encoded: ", y_test_scaled_encoded) # will print the encoded discrete values

# Use a logistic regression model
# instantiate the model
logreg = LogisticRegression(solver="liblinear")
# fit the model with data
logreg.fit(X_train_scaled,y_test_scaled_encoded)

# Step 4: Predict the response for a new observation
# New observations are called "out-of-sample" data
# Uses the information it learned during the model training process
X_train_new = [[3, 5, 4, 2], [5, 4, 3, 2]]
test_model = logreg.predict(X_train_new)
print(test_model)