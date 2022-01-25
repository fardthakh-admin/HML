from django.urls import path,reverse
from . import views
from .views import *
app_name='patients_heart_model'
urlpatterns = [
    path('/<int:user_id>', views.update_profile, name='index'),
    path('/AddFamily',views.family_page,name='familypage'),
    
    ]

