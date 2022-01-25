from django.contrib import admin
from .models import *
from .forms import *
from import_export.admin import ImportExportModelAdmin
from import_export import resources
# class ArticleAdmin(admin.ModelAdmin):
#     list_display = ("slug","title") # display these table columns in the list view
#     def changelist_view(self,request,extra_context=None):
#         xdata = ["General Content", "At Risk Content", "Diabetes Content"]
#         Atrisk=Article.objects.filter(tags__name__exact="TenYearCHD").count()
#         General=Article.objects.filter(tags__name__exact="GeneralContent").count()
#         Diabetes=Article.objects.filter(tags__name__exact="diabetes").count()
#         ydata = [General, Atrisk, Diabetes]

#         extra_serie1 = {"tooltip": {"y_start": "", "y_end": " cal"}}
#         chartdata = {
#             'x': xdata, 'name1': '', 'y1': ydata, 'extra1': extra_serie1,
#         }
#         charttype = "discreteBarChart"
#         context = {
#             'charttype': charttype,
#             'chartdata': chartdata,
#         }

#         resource_class=ArticleResource
#         return super().changelist_view(request, extra_context=context)

class ArticleResource(resources.ModelResource):
    class Meta:
        model=Article



class ArticleAdmin(ImportExportModelAdmin):
    resource_class = ArticleResource


admin.site.register(Article,ArticleAdmin)




        
class ReportAdmin(admin.ModelAdmin):
    form=ReportForm
    list_display=('uploaded_by',)
    def save_model(self, request, obj, form, change):
        if not obj.uploaded_by.id:
            obj.uploaded_by = request.user
        obj.save()    


class ActivityResource(resources.ModelResource):
    class Meta:
        model=Activity



class ActivityAdmin(ImportExportModelAdmin):
    resource_class = ActivityResource


admin.site.register(Activity,ActivityAdmin)


admin.site.register(Report,ReportAdmin)
