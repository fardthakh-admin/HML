from django import forms
from .models import Report
class ReportForm(forms.ModelForm):
    class Meta:
        model=Report
        fields=('report',)
    def uploadeby(self):
        if not self.cleaned_data['uploaded_by']:
            return User()
        return self.cleaned_data['uploaded_by']