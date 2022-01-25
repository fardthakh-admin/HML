from django.db import models
from taggit.managers import TaggableManager
from hitcount.models import  HitCount
from hitcount.views import HitCountMixin
from django.contrib.contenttypes.fields import GenericRelation
from django.utils.encoding import python_2_unicode_compatible
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# seed the pseudorandom number generator
from random import seed
from random import random


@python_2_unicode_compatible
class Article(models.Model,HitCountMixin):
    title=models.CharField(max_length=120)
    body=models.TextField()
    tags=TaggableManager(blank=True)
    seed(1)
    slug = models.SlugField(unique=True, max_length=200,default=random())
    hit_count_generic = GenericRelation(HitCount, object_id_field='object_pk',
     related_query_name='hit_count_generic_relation')
    def __str__(self):
        return self.title
    

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super(Article, self).save(*args, **kwargs)

class Report(models.Model):
    report=models.FileField(upload_to="reports/")
    uploaded_by=models.ForeignKey(User,on_delete=models.CASCADE,blank=True)
    upload_date=models.DateTimeField(auto_now_add=True)
    def __str__(self):        
        return str(self.id)

def post_save_receiver(sender, instance, created, **kwargs):
    pass

post_save.connect(post_save_receiver, sender=settings.AUTH_USER_MODEL)

class Activity(models.Model,HitCountMixin):
    Title=models.CharField(max_length=120)
    description=models.CharField(max_length=120)
    tags=TaggableManager(blank=True)
    date=models.DateField()
    def __str__(self):        
        return str(self.Title)