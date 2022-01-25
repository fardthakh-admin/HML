"""HML URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic.base import TemplateView
from Content_Management.views import *
from Patients_Records.views import *
from Patients_Heart_Model.views import MemberAutocomplete
admin.site.site_header = 'Health Care ML admin'

admin.site.site_title = 'HML admin'
admin.site.site_url = 'http://HML.com/'
admin.site.index_title = 'HML administration'
urlpatterns = [
    path('admin_tools_stats/', include('admin_tools_stats.urls')),
    path('admin_tools/', include('admin_tools.urls')),
    path('Patients_Records', include('Patients_Records.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('Content_Management',include('Content_Management.urls',namespace="CM")),
    path('Patients_Heart_Model',include('Patients_Heart_Model.urls',namespace="Patients_HM")),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('hitcount/', include(('hitcount.urls', 'hitcount'), namespace='hitcount')),
    path('detail/<slug:slug>/',ArticleDetailView.as_view(), name='single_article'),
    path('dailydiet',include('dailydiet.urls',namespace="Diet")),
    path('patient-autocomplete',MemberAutocomplete.as_view(),name='patient-autocomplete'),



]

