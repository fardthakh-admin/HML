from django.contrib import admin
from django.contrib.admin import AdminSite
from .models import *
from import_export import resources
from Patients_Records.models import *
from import_export.admin import ImportExportModelAdmin
from django.http import HttpResponseRedirect
import sys, os
sys.path.append(os.path.abspath(os.path.join('..', 'common')))
from common.HSmodel import *


class patientResource(resources.ModelResource):

    class Meta:
        model = Patient_basic_record

class patientAdmin(ImportExportModelAdmin):
    resource_class = patientResource
@admin.register(Patient_basic_record)
class Patient_basic_recordAdmin(admin.ModelAdmin):
    list_display = ( "id", "TenYearCHD")
    def changelist_view(self,request,extra_context=None):
        xdata = ["Patient at risk ", "patient not at risk", "high glucose",'overweight']
        patientscount=Patient_basic_record.objects.count()
        risk=Patient_basic_record.objects.filter(TenYearCHD=True).count()/patientscount
        notrisk=Patient_basic_record.objects.filter(TenYearCHD=True).count()/patientscount
        diabetes=Patient_basic_record.objects.filter(glucose__gte=180).count()/patientscount
        overweight=Patient_basic_record.objects.filter(BMI__gte=30).count()/patientscount
        ydata = [risk,notrisk,diabetes,overweight]
        chartdata = {'x': xdata, 'y': ydata}
        charttype = "pieChart"
        chartcontainer = 'piechart_container'
        context = {
        'charttype': charttype,
        'chartdata': chartdata,
        'chartcontainer': chartcontainer,
        'extra': {
            'x_is_date': False,
            'x_axis_format': '',
            'tag_script_js': True,
            'jquery_on_ready': False,
        }
        }
        return super().changelist_view(request, extra_context=context)


def get_urls(self):
    urls = super().get_urls()
    my_urls = [
        path('heart',runscript),
    ]

    return my_urls + urls

def runscript(self):
    OldPatientRecordClassification()
    return HttpResponseRedirect('/admin/Patients_Records/patient_basic_record/')

# admin.site.register(Patient_basic_record, patientAdmin) #uncomment to add import /export functionality

# class HMLAdminSite(AdminSite):
#     AdminSite.index_template='new_index.html'
#     def get_urls(self):
#         urls=super().get_urls()
#         my_urls=[path('indexchart/',AdminSite.admin_view(self.indexcharts)),
#         ]
#         return urls+my_urls
#     def indexcharts(self,request):
#         #this is a view function
#         xdata = ["Patient at risk ", "patient not at risk", "high glucose",'overweight']
#         patientscount=Patient_basic_record.objects.count()
#         risk=Patient_basic_record.objects.filter(TenYearCHD=True).count()/patientscount
#         notrisk=Patient_basic_record.objects.filter(TenYearCHD=True).count()/patientscount
#         diabetes=Patient_basic_record.objects.filter(glucose__gte=180).count()/patientscount
#         overweight=Patient_basic_record.objects.filter(BMI__gte=30).count()/patientscount
#         ydata = [risk,notrisk,diabetes,overweight]
#         chartdata = {'x': xdata, 'y': ydata}
#         charttype = "pieChart"
#         chartcontainer = 'piechart_container'
#         context = {
#         'charttype': charttype,
#         'chartdata': chartdata,
#         'chartcontainer': chartcontainer,
#         'extra': {
#             'x_is_date': False,
#             'x_axis_format': '',
#             'tag_script_js': True,
#             'jquery_on_ready': False,
#         }
#         }
#         request.current_app=self.name
#         self.admin_site.each_context(request)
#         return TemplateResponse(request,'new_index.html',context)
# admin_site=HMLAdminSite(name="HMLadmin")
