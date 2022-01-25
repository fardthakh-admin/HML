from django.urls import path,re_path
from django.conf.urls import include
from dailydiet.views import *
app_name='dailydiet'
urlpatterns = [
    path('/dailymealform',DietForm,name="dailymeal"),
    ]

