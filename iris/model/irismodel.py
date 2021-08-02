import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split as tts
from sklearn.ensemble import RandomForestClassifier
import joblib

iris = pd.read_csv('Iris.csv')

feature_columns = ['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']
target_columns = ['Species']

lbl_en = LabelEncoder()
iris[target_columns] = lbl_en.fit_transform(iris[target_columns])

speciesdict = {0:'Iris-setosa',1:'Iris-versicolor',2:'Iris-virginica'}

x_train,x_test,y_train,y_test = tts(iris.drop('Species',axis=1),iris.Species,test_size=0.4,random_state=42)

rf_clf = RandomForestClassifier(n_jobs=-1,n_estimators=100,max_depth=4)
rf_clf.fit(x_train,y_train)

joblib.dump(rf_clf,'irismodel.pkl')

