from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.conf import settings
from django_pandas.managers import DataFrameManager
# Create your models here.
class Meal(models.Model):
    meal_name = models.CharField(max_length=120)
    fat = models.IntegerField()
    calories = models.IntegerField()
    protein = models.IntegerField()
    def __str__(self):
        return self.meal_name

class Daily_Meal(models.Model):
    breakfast = models.ForeignKey(Meal,related_name="breakfast", 
    on_delete=models.CASCADE,blank=True)
    lunch = models.ForeignKey(Meal,related_name="lunch",
    on_delete=models.CASCADE,blank=True)
    dinner = models.ForeignKey(Meal,related_name="dinner",
    on_delete=models.CASCADE,blank=True)
    date=models.DateField(auto_now_add=True,)
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True,related_name='diet_patient')
    Sad = 1
    SSad = 2
    Nutr = 3
    SHappy =4
    Happy = 5
    CHOICES = (
        (Sad, 'Sad'),
        (SSad, 'Slightly Sad'),
        (Nutr, 'Nutral'),
        (SHappy, 'Slightly Happy'),
        (Happy, 'Happy'),
    )
    reaction = models.IntegerField(max_length=100,
        choices=CHOICES, 
        default= 3)
    def __str__(self):
        return str(self.date)
    objects = DataFrameManager()


def post_save_receiver(sender, instance, created, **kwargs):
    pass

post_save.connect(post_save_receiver, sender=settings.AUTH_USER_MODEL)

