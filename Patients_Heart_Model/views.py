from django.shortcuts import render,redirect
from .models import *
from .forms import *
from dal import autocomplete


# Create your views here.
def update_profile(request, user_id):
    user = User.objects.get(pk=user_id)
    user.save()

def family_page(request):
    if request.method=='POST':
        form=FamilyForm(request.POST)
        if form.is_valid():
            

            form.save()
            return redirect("CM:content for current user")
    else:
        form = FamilyForm()
    return render(request, 'family.html', {
        'form': form})

class MemberAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated:
            return Patient_Classified.objects.none()

        qs = Patient_Classified.objects.all()

        if self.q:
            qs = qs.filter(user__username__istartswith=self.q)

        return qs                                