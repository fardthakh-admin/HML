from django.urls import path,re_path
from django.conf.urls import include
from Content_Management.views import *
from . import views

app_name='Article'
urlpatterns = [
    path('/all',views.AllArticles,name="all articles"),
    path('/<str:tag>/',views.ListOfArticles,name="similar_articles"),
    path('/',views.ContentBasedOnUser,name="content for current user"),
    path('/submit_report',views.model_form_upload,name='submit_report'),
    path('/MyProfile',views.MyProfile,name='myprofile'),
    path('/Medications',views.medication,name="medicationcalendar"),
    path('/appointment', views.appointment, name="appointmentcalendar"),
    path('/FamilyHealth',views.Get,name='FamilyHealth'),
    path("/allac",views.AllActivities,name="all activities")
]
