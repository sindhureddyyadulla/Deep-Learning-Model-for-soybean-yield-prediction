from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
import tensorflow as tf
from keras import Sequential
from tensorflow import keras
import numpy as np
import pandas as pd 
import pickle  
import csv,io
from numpy import loadtxt
from keras.models import load_model
# Create your views here.
#data_csv = pd.read_csv('input.csv')
#data = data_csv.iloc[:,394].values
def home(home):
    return render(home, 'home.html')
def details(details):
    return render(details,'details.html')
def about(about):
    return render(about,'about.html')
def uploadfile(result):
    #if not csv_file.name.endswith('.csv'):
       # messages.error(uploadfile, 'Please upload a .csv file.')
    #if result.method == "POST":
        #data_csv = result.FILES['filename'].read()    
    template="uploadfile.html"
     #if not csv_file.name.endswith('.csv'):
       # messages.error(result, 'Please upload a .csv file.')
    return render(result,template)
        
def result(result): 
    model=load_model('Yield.h5')
    if result.method == "POST":
        csv_file = result.FILES['filename']
        #stream = io.StringIO(csv_file.read().decode("UTF8"), newline=None)
        #file = pd.read_csv(stream)
        file=pd.read_csv(csv_file, encoding='utf8')
        df=pd.DataFrame(file)
        x=df.iloc[:,0:394]
        y=model.predict(x)
        ans=np.mean(y)
        return render(result,'result.html',{'ans':ans})
    return render(result,'result.html')    
    '''
    #open('Yield.sav', 'a').close()
    cls=pickle.load(open('Yield.sav','rb'))
    #cls.load_state_dict(pickle.load('Yield.sav', map_location='cpu'))
    #with open("filename","r") as csvfile:
        #data_csv=csv.reader(cYsvfile)
    if result.method == "POST":
        csv_file = result.FILES['filename']
        data_csv = pd.read_csv(csv_file)
        data_npz=np.array(data_csv)
        df=data_csv
        df_x=df.iloc[:,0:394]
        y=cls.predict(df_x)
        ans=np.mean(y)  
        return render(result,'uploadfile/result.html',{'ans':ans})
    return render(result,'result.html')
'''

    