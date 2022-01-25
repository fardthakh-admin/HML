from django import forms
from .models import *
from dal import autocomplete
class FamilyForm(forms.ModelForm):

        class Meta:
            model=Family
            fields=('__all__')
            widgets ={
                'members':autocomplete.ModelSelect2Multiple(url='patient-autocomplete')
            }