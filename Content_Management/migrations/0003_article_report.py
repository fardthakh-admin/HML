# Generated by Django 2.2.6 on 2020-02-02 15:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import hitcount.views
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Content_Management', '0002_auto_20200202_1529'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('report', models.FileField(upload_to='reports/')),
                ('upload_date', models.DateTimeField(auto_now_add=True)),
                ('uploaded_by', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('body', models.TextField()),
                ('slug', models.SlugField(default=0.13436424411240122, max_length=200, unique=True)),
                ('tags', taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
            bases=(models.Model, hitcount.views.HitCountMixin),
        ),
    ]