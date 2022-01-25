from django.shortcuts import render,render_to_response
from django.http import HttpResponse
from Patients_Records.models import Patient_basic_record
from .models import *
import sys, os
sys.path.append(os.path.abspath(os.path.join('..', 'common')))
from common.HSmodel import *

def index(request):
    return HttpResponse("you are in patients records")

    
def SinglePatientRecords(request,PatientID):
    PatientRecords=Patient_basic_record.objects.filter(Patient_ID__id=PatientID)
    df = read_frame(PatientRecords)
    return HttpResponse(df.to_html())
    #return render(request, 'mlmodel_qs.html')
def ModelAccuracy(request):
    score=ClassifierAccuracy()
    context={
        'score':score,
    }
    return render(request,'accuracy.html',context)
def updateunlabeled(request):
    test=OldPatientRecordClassification()
    return HttpResponse(test)
