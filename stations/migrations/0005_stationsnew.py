# Generated by Django 4.2.1 on 2023-08-05 07:42

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stations', '0004_trainfullinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='StationsNew',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stationCode', models.CharField(default='')),
                ('stationName', models.CharField(default='')),
                ('latitude', models.FloatField(default=0.0)),
                ('longitude', models.FloatField(default=0.0)),
                ('city', models.CharField(default='')),
                ('state', models.CharField(default='')),
                ('postCode', models.IntegerField(default=0)),
                ('wifi', models.IntegerField(default=0)),
                ('near', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(default=''), size=None)),
                ('division', models.CharField(default='')),
                ('platforms', models.CharField(default='')),
                ('category', models.CharField(default='')),
                ('score', models.IntegerField(default=0)),
                ('neighbours', models.CharField(default='')),
                ('sound', models.CharField(default='')),
                ('stname_te', models.CharField(default='')),
                ('stname_bn', models.CharField(default='')),
                ('stname_tn', models.CharField(default='')),
                ('stname_gu', models.CharField(default='')),
                ('stname_ta', models.CharField(default='')),
                ('stname_kn', models.CharField(default='')),
                ('stname_ml', models.CharField(default='')),
                ('stname_mr', models.CharField(default='')),
            ],
        ),
    ]
