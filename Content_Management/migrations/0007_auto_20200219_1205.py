# Generated by Django 2.2.6 on 2020-02-19 12:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Content_Management', '0006_activity'),
    ]

    operations = [
        migrations.RenameField(
            model_name='activity',
            old_name='Title',
            new_name='title',
        ),
    ]