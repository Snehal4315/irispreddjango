from django.shortcuts import render
import joblib
import pandas as pd
from .models import irisdata

# Create your views here.
def index(request):
    return render(request,'home.html')


def result(request):
    if request.method == "POST":
        features = {}
        features['sl'] = request.POST.get('sl') 
        features['sw'] = request.POST.get('sw') 
        features['pl'] = request.POST.get('pl') 
        features['pw'] = request.POST.get('pw') 

        final_features = pd.DataFrame({'x':features}).transpose()
        model = joblib.load('iris/model/Iris.pkl')
        result = model.predict(final_features)[0]
        iris = ''

        if(result == 0):
            iris = 'Iris-Setosa'
        elif(result == 1):
            iris = 'Iris-Versicolor'
        else:
            iris = 'Iris-Verginica'

        db = irisdata(Sepallength=features['sl'],Sepalwidth=features['sw'],Petallength=features['pl'],Petalwidth=features['pw'],Irispred=iris)
        db.save()
        return render(request,'home.html',{'result':iris})