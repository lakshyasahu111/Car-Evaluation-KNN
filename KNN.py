#Importing Libraries
import numpy as np
import pandas as pd
from sklearn import neighbors,metrics
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

#Importing Dataset
data = pd.read_csv('KNN/car+evaluation/car.data')

# Adding Labels to the Data
#X
X=data[[
    'buying',
    'main',
    'safety'
]].values

#Y
y=data[[
    'class'
]]

# Converting the Data using Label Encoder
#X
Le=LabelEncoder()
for i in range(len(X[0])):
    X[:,i]=Le.fit_transform(X[:,i])
# print(X,y)
# print(data.head())
# print(X)

#Y (Using Mapping)
label_mapping={
    'unacc':0,
    'acc':1,
    'good':2,
    'vgood':3
}
y['class']=y['class'].map(label_mapping)
y=np.array(y)
# print(y)

# Creating KNN-Object
knn=neighbors.KNeighborsClassifier(n_neighbors=25,weights='uniform')

#Splitting and Trainig the data
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2)
knn.fit(X_train,y_train)

#Making Predictions and Testing Accuracy
prediction=knn.predict(X_test)
accuracy=metrics.accuracy_score(y_test,prediction)

print("Prediction: ",prediction)
print("Accuracy of The Model is : ",accuracy)