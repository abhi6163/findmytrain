# Generated by Django 4.2.1 on 2023-07-26 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RouteInfo1',
            fields=[
                ('trainCode', models.CharField(max_length=25, primary_key=True, serialize=False)),
                ('route', models.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name='RouteStations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stnCode', models.CharField(max_length=10)),
                ('stnName', models.CharField(max_length=180)),
                ('longitude', models.FloatField()),
                ('latitude', models.FloatField()),
                ('isHalt', models.IntegerField()),
                ('distanceFromOrigin', models.IntegerField()),
                ('daySinceDepart', models.IntegerField()),
                ('schedulledArrival', models.CharField()),
                ('schedulledDepart', models.CharField()),
                ('slNo', models.IntegerField()),
                ('platformNo', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Stations',
            fields=[
                ('Latitude', models.FloatField()),
                ('Longitude', models.FloatField()),
                ('StationCode', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('StationName', models.CharField(default='no_name', max_length=256)),
                ('Wifi', models.IntegerField()),
                ('NameSoundex', models.CharField(max_length=120)),
                ('Score', models.IntegerField(blank=True, default=0)),
            ],
        ),
    ]
