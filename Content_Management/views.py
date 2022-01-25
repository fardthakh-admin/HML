from django.shortcuts import render, get_object_or_404,render_to_response,redirect
from taggit.models import Tag
from .models import *
from django.http import HttpResponse,HttpResponseRedirect
from hitcount.views import HitCountDetailView
from django.conf.urls import include
from django.views.generic.list import ListView
from .forms import *
from django.core.files.storage import FileSystemStorage
from Patients_Records.models import *
from Patients_Heart_Model.models import * 
from dailydiet.models import *
import pandas as pd
from django_pandas.io import read_frame
def ListOfArticles(request,tag):
    #list articles that contain a certain tag
    tags = Tag.objects.filter().values_list('name')
    
    articles = Article.objects.filter(tags__name__icontains=tag)
    context = {
        
        'articles':articles,
    }
    return render(request, 'Content_Management/listofarticles.html', context)

def AllArticles(request):
    articles=Article.objects.all()
    
    context = {
        
        'articles':articles,
    }
    return render(request, 'Content_Management/listofarticles.html', context)
def ContentBasedOnUser(request):
    tag=request.user.patient.patient_basic_record_set.last().TenYearCHD
    if tag:
        tag="TenYearCHD"
        articles = Article.objects.filter(tags__name__exact=tag)
    else :
        tag="GeneralContent"
        articles=Article.objects.filter(tags__name__exact=tag)
     #request.user=>currentuser |patient=>1-to-1 field|    
    
    context = {
        
        'articles':articles,
    }
    return render(request, 'Content_Management/listofarticles.html', context)


class ArticleListView(ListView):
    model = Article
    context_object_name = 'articles'
    template_name = 'Content_Management/listofarticles.html'
    
class ArticleDetailView(HitCountDetailView):
    model = Article
    template_name = 'Content_Management/article.html'
    context_object_name = 'article'
    slug_field = 'slug'
    # set to True to count the hit
    count_hit = True

    def get_context_data(self, **kwargs):
        context = super(ArticleDetailView, self).get_context_data(**kwargs)
        context.update({
        'popular_posts': Article.objects.order_by('-hit_count_generic__hits')[:3],
        })
        return context

def model_form_upload(request):
    if request.method=='POST':
        form=ReportForm(request.POST,request.FILES)
        if form.is_valid():
            form=form.save(commit=False)
            form.uploaded_by=request.user
            form.save()
            return redirect("CM:content for current user")
    else:
        form = ReportForm()
    
    
    return render(request, 'Content_Management/submitreport.html', {
        'form': form
    })
def MyProfile(request):
    patientID=Patient_Classified.objects.filter(user=request.user).last().id
    recordBMI=Patient_basic_record.objects.filter(Patient_ID__id=patientID).last().BMI
    Glucose=Patient_basic_record.objects.filter(Patient_ID__id=patientID).last().glucose
    totchol=Patient_basic_record.objects.filter(Patient_ID__id=patientID).last().totChol
    #correlation calculation starts here 

    qsmeals=Meal.objects.all()
    qs=Daily_Meal.objects.filter(user=request.user)
    totfat,cal,prot,react=[],[],[],[]
    for e in qs:
        fat=0
        calories=0
        protien=0
        fat=e.breakfast.fat + e.lunch.fat +e.dinner.fat
        calories=e.breakfast.calories + e.lunch.calories +e.dinner.calories
        protein=e.breakfast.protein + e.lunch.protein +e.dinner.protein
        reaction=int(e.reaction)
        react.append(reaction)
        totfat.append(fat)
        cal.append(calories)
        prot.append(protein)
    totals={'Fat':totfat,'Calories':cal,'Protein':prot}
    df=pd.DataFrame(totals)
    
    # df=df.to_html()
    react=pd.Series(react)  
    corr=df.corrwith(react)
    corr=corr.argmax()
    dailyfat=sum(totfat)
    dailyprotein=sum(prot)
    dailycalories=sum(cal)

    context={
        
        "user":request.user.first_name,
        "BMI":recordBMI,
        "glucose":Glucose,
        "totchol":totchol,
        "nutriant":corr,
        "dailyfat":dailyfat,
        "dailyprotein":dailyprotein,
        "dailycalories":dailycalories,

        }
    return render(request,'Content_Management/MyProfile.html',context)
def medication(request):
    return render(request,'Content_Management/medicationcalendar.html')
def appointment(request):
    return render(request,"Content_Management/appointmentcalendar.html")
def Get(request):
    return render(request,"Content_Management/family.html")






def AllActivities(request):
    activities=Activity.objects.all()
    
    context = {
        
        'activities':activities,
    }
    return render(request, 'Content_Management/listofactivities.html', context)

# def corrnutriants(request):
#     qsmeals=Meal.objects.all()
#     qs=Daily_Meal.objects.filter(user=request.user)
#     totfat,cal,prot,react=[],[],[],[]
#     for e in qs:
#         fat=0
#         calories=0
#         protien=0
#         fat=e.breakfast.fat + e.lunch.fat +e.dinner.fat
#         calories=e.breakfast.calories + e.lunch.calories +e.dinner.calories
#         protein=e.breakfast.protein + e.lunch.protein +e.dinner.protein
#         reaction=int(e.reaction)
#         react.append(reaction)
#         totfat.append(fat)
#         cal.append(calories)
#         prot.append(protein)
#     totals={'TotFat':totfat,'TotCalories':cal,'TotProtein':prot}
#     df=pd.DataFrame(totals)
#     # df=df.to_html()
#     react=pd.Series(react)  
#     corr=df.corrwith(react)
#     corr=corr.to_frame()
#     corr=corr.to_html()
#     return HttpResponse(corr)