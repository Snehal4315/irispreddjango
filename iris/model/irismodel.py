import pandas as pd
from sklearn.preprocessing import LabelEncoder
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split as tts
import joblib

iris = pd.read_csv('iris/model/Iris.csv')

feature_columns = ['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']
target_columns = ['Species']

lbl_en = LabelEncoder()
iris[target_columns] = lbl_en.fit_transform(iris[target_columns])

speciesdict = {0:'Iris-setosa',1:'Iris-versicolor',2:'Iris-virginica'}

x_train,x_test,y_train,y_test = tts(iris.drop('Species',axis=1),iris.Species,test_size=0.2,random_state=42)

xgb = XGBClassifier()
xgb.fit(x_train,y_train)

joblib.dump(xgb,'iris/model/irismodel.pkl')

