from django.db import models
import datetime
from django_pandas.managers import DataFrameManager
from Patients_Heart_Model.models import Patient_Classified
from django.contrib import admin
class Patient_basic_record(models.Model):
    Patient_ID=models.ManyToManyField(Patient_Classified)
    date_sent = models.DateTimeField(auto_now_add=True,editable=False,null=True)
    Patient_age=models.IntegerField(max_length=10,)
    Current_Smoker=models.BooleanField(default=False)
    CigsPerDay=models.IntegerField(max_length=10)
    BPMeds=models.BooleanField()
    PrevalentStroke=models.IntegerField(max_length=10)
    PrevalentHyp=models.IntegerField(max_length=10)
    diabetes=models.BooleanField()
    totChol=models.IntegerField(max_length=10)
    sysBP=models.IntegerField(max_length=10)
    diaBP=models.IntegerField(max_length=10)
    BMI=models.FloatField(max_length=10)
    heartRate=models.IntegerField(max_length=10)
    glucose=models.IntegerField(max_length=10)
    TenYearCHD=models.NullBooleanField()
    objects = DataFrameManager()
    def __str__(self):
        return str(self.id)
    
    class Meta :
        ordering = ['date_sent'] # records for each patient are ordrered by date 





