from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_pandas.managers import DataFrameManager

# Create your models here.
class Patient_Classified(models.Model):
    # TenYearCHD=models.BooleanField()
    # Patient_Records=models.ManyToManyField(Patient_basic_record,null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True,related_name='patient')
    objects = DataFrameManager()
    def __str__(self):
        return self.user.username
@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
class Family(models.Model):
    FamilyName=models.CharField(max_length=100,verbose_name='familyname')
    members=models.ManyToManyField(Patient_Classified, verbose_name=("member"))
    def __str__(self):
        return self.FamilyName
