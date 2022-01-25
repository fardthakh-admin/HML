from django.urls import path
from . import views
from .admin import runscript
urlpatterns = [
    path('', views.index, name='index'),
    path('/ModelAccuracy',views.ModelAccuracy,name="modelaccuracy"),
    path('/PatientRecords/<int:PatientID>',views.SinglePatientRecords,name="singlepatientrecord"),
    path('/updateunlabeled',views.updateunlabeled,name="updateunlabeled"),
    path('/heart',runscript)
]