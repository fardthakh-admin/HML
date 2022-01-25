from django import forms
from .models import *
class DailyMealForm(forms.ModelForm):

    class Meta:
        model=Daily_Meal
        fields=('breakfast','lunch','dinner','reaction',)
    def uploadeby(self):
        if not self.cleaned_data['user']:
            return User()
        return self.cleaned_data['user']