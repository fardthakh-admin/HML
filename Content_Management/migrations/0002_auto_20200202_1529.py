# Generated by Django 2.2.6 on 2020-02-02 15:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Content_Management', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='report',
            name='uploaded_by',
        ),
        migrations.DeleteModel(
            name='Article',
        ),
        migrations.DeleteModel(
            name='Report',
        ),
    ]
