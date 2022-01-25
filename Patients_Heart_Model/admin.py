from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from django.contrib.auth.admin import UserAdmin as BaseAdmin
from django.contrib.auth.models import User



class UserResource(resources.ModelResource):
    class Meta:
        model = User
        fields = ('id','username','first_name', 'last_name', 'email')
        

# class UserAdmin(BaseAdmin, ImportExportModelAdmin):
#     resource_class = UserResource

admin.site.unregister(User)
admin.site.register(User, BaseAdmin)


class patientClassResource(resources.ModelResource):

    class Meta:
        model = Patient_Classified

class patientClassAdmin(ImportExportModelAdmin):
    resource_class = patientClassResource
class familyclassadmin(admin.ModelAdmin):
    filter_horizontal=('members',)

admin.site.register(Patient_Classified,patientClassAdmin)
admin.site.register(Family,familyclassadmin)