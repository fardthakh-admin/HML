
from django.shortcuts import render, get_object_or_404,render_to_response,redirect
import pandas as pd
from django_pandas.io import read_frame
from django.shortcuts import render,HttpResponse
from .forms import *
from django_pandas.managers import DataFrameManager

# Create your views here.
def DietForm(request):
    if request.method=='POST':
        form=DailyMealForm(request.POST)
        if form.is_valid():
            form=form.save(commit=False)
            form.user=request.user
            form.save()
            return redirect("CM:content for current user")
    else:
        form = DailyMealForm()
    
    
    return render(request, 'dailymealform.html', {
        'form': form
    })


