from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.
import joblib
import pandas as pd
from pymongo import MongoClient
client=MongoClient('localhost', 27017)

db=client['mpgDatabase']
collectionD=db['mpgTable']
Reload_Model = joblib.load('./models/MPG_MODEL.pkl')
def index(request):
    template=loader.get_template('index.html')
    context={'a':''}
    return HttpResponse(template.render(context,request))
def predictMPG(request):
    temp={};
    temp['cylinders']=request.POST.get('cylinderval')
    temp['displacement'] = request.POST.get('dispval')
    temp['horsepower'] = request.POST.get('hrspval')
    temp['weight'] = request.POST.get('weightval')
    temp['acceleration'] = request.POST.get('accval')
    temp['model_year'] = request.POST.get('modelval')
    temp['origin']=request.POST.get('originval')
    temp2=temp.copy()
    temp2['model year']=temp['model_year']
    testdata=pd.DataFrame({'x':temp2}).transpose()
    scoreval=Reload_Model.predict(testdata)[0]
    context={'a': 'Try Again', 'b':scoreval,'c':'Your Score is : ', 'temp':temp2}

    return render(request,'index.html',context)