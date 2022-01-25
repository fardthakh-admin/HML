import json
import sys
sys.setrecursionlimit(10000)
from django_pandas.io import read_frame
import pandas as pd
import numpy as np
from pandas.io.json import json_normalize
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix,accuracy_score
from sklearn.model_selection import train_test_split
from collections import OrderedDict
from Patients_Records.models import Patient_basic_record
from Patients_Heart_Model.models import Patient_Classified
from django.db import connection
from sklearn.feature_selection import SelectKBest
import matplotlib.pyplot as plt
    

def ClassifierAccuracy(updaterecord=False):
    qs=Patient_basic_record.objects.all()
    heart_df=qs.to_dataframe(index="id")
    heart_df.drop(["date_sent"],axis=1,inplace=True) 
    heart_df.dropna(axis=0,inplace=True)
    labeled=heart_df["TenYearCHD"].shape[0]
    y=heart_df.iloc[:labeled,-1].values
    X=heart_df.iloc[:labeled,:-1].values

    y=y.astype("bool")
    x_train, x_test, y_train, y_test = train_test_split(X ,y,test_size=0.15,random_state=0)
    rfc= RandomForestClassifier(random_state=1)
    rfc.fit(x_train,y_train)
    y_pred=rfc.predict(x_test)
    score=accuracy_score(y_test,y_pred)
    if updaterecord:
        return rfc
    features=heart_df.columns[0:-1]
    importances = rfc.feature_importances_
    indices = np.argsort(importances)

    fig=plt.figure(1)
    fig.set_size_inches(18.5, 10.5, forward=True)
    plt.title('Feature Importances')
    plt.barh(range(len(indices)), importances[indices], color='b', align='center')
    plt.yticks(range(len(indices)), features[indices])
    plt.xlabel('Relative Importance')
    plt.savefig('Importance.png')
    return score
def OldPatientRecordClassification():
    #update the TenYearCHD of unlabeled patients
    unlabeledrecords=Patient_basic_record.objects.filter(TenYearCHD=None)
    ##iterate over unlabeled records of old patients #we pass in the id of the classified patient with the first unlabeled record 
         
    while (unlabeledrecords.exists()):
        patientID=unlabeledrecords[0].Patient_ID.all()[0].id
        PatientRecords=Patient_basic_record.objects.filter(Patient_ID__id=patientID) 
        df=PatientRecords.to_dataframe(index="id")
        df.drop(["date_sent"],axis=1,inplace=True) #date sent is unnecessary here 
        X=df.iloc[-1,:-1].values
        X=X.reshape(1,-1)
        rfc=ClassifierAccuracy(updaterecord=True)
        y=rfc.predict(X) #y is the label (TenYearCHD ) of the new record of the old patient 
        labeledrecord=Patient_basic_record.objects.filter(Patient_ID__id=patientID).last()
        labeledrecord.TenYearCHD=y 
        labeledrecord.save(update_fields=["TenYearCHD"])
        unlabeledrecords=Patient_basic_record.objects.filter(TenYearCHD=None)
 # for now we only return the new record which we labeled using this function for the test view in patients_ Records
# def updatelabels():
