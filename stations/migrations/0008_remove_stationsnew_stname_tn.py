# Generated by Django 4.2.1 on 2023-08-06 10:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stations', '0007_stationsnew_near'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stationsnew',
            name='stname_tn',
        ),
    ]
