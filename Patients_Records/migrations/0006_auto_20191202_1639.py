# Generated by Django 2.2.6 on 2019-12-02 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Patients_Records', '0005_auto_20191201_1514'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient_basic_record',
            name='Patient_ID',
            field=models.ManyToManyField(to='Patients_Heart_Model.Patient_Classified'),
        ),
    ]
