from django.db import models
from django.contrib.postgres.fields import ArrayField

# # Create your models here.
# class Trains(models.Model):
#     """Making model for train search"""
#     name = models.CharField(max_length=255)
#     code = models.CharField(max_length=5)
#     fromStation = models.CharField(max_length=60)
#     toStation = models.CharField(max_length=60)

    # def __str__(self) -> str:
    #     return self.code
class StationsNew(models.Model):
    """Stations full information"""
    stationCode=models.CharField(default='',primary_key=True)
    stationName=models.CharField(default='')
    latitude=models.FloatField(default=0.0)
    longitude=models.FloatField(default=0.0)
    city=models.CharField(default='')
    state=models.CharField(default='')
    postCode=models.IntegerField(default=0)
    wifi=models.IntegerField(default=0)
    near=models.CharField(default='')
    division=models.CharField(default='')
    platforms=models.CharField(default='')
    category=models.CharField(default='')
    score=models.IntegerField(default=0)
    neighbours=models.CharField(default='')
    sound=models.CharField(default='')
    stname_te=models.CharField(default='')
    stname_hi=models.CharField(default='')
    stname_bn=models.CharField(default='')
    stname_ta=models.CharField(default='')
    stname_gu=models.CharField(default='')
    stname_kn=models.CharField(default='')
    stname_ml=models.CharField(default='')
    stname_mr=models.CharField(default='')
    def __str__(self) -> str:
        return self.stationCode
class TrainInfo(models.Model):
    '''About Train'''
    trainCode = models.CharField(max_length=15,primary_key=True,default='')
    trName=models.CharField(default='')
    srcStation = models.JSONField(default='{}')
    destStation=models.JSONField(default='{}')
    distance=models.IntegerField(default=0)
    timeTakeInSec=models.IntegerField(default=0)
    duration=models.CharField(default='')
    halts=models.IntegerField(default=0)
    depTimeFromSrc=models.CharField(default='')
    arrTimeAtDest=models.CharField(default='')
    avgSpeed=models.CharField(default='')
    trname_telgu=models.CharField(default='')
    trname_hindi=models.CharField(default='')
    trname_bengali=models.CharField(default='')
    trname_tamil=models.CharField(default='')
    trname_kannada=models.CharField(default='')
    trname_malyalam=models.CharField(default='')
    trname_marathi=models.CharField(default='')
    trname_gujrati=models.CharField(default='')
    coach=ArrayField(models.CharField(default=''))
    reversal=ArrayField(models.CharField(default='',blank=True),blank=True)
    trainType=models.CharField(default='')
    inaugural=models.CharField(default='')
    wiki=models.CharField(default='')
    sound=models.CharField(default='')
    rake=models.CharField(default='')
    trainRunsOn=models.CharField(default='')
    haltsList=ArrayField(models.CharField(default=''),blank=True)
    arrDayTimeList=ArrayField(ArrayField(models.CharField(),size=2,blank=True),blank=True,default=[''])
    depDayTimeList=ArrayField(ArrayField(models.CharField(),size=2,blank=True),blank=True,default=[''])
    haltsDistList=ArrayField(models.IntegerField(default=0,blank=True),blank=True,default=[0])
    platformList=ArrayField(models.CharField(default=0,blank=True,max_length=20),blank=True,default=[''])
    def __str__(self) -> str:
        return self.trainCode
class Stations(models.Model):
    """Stations Information"""
    Latitude=models.FloatField()
    Longitude=models.FloatField()
    StationCode=models.CharField(max_length=10,primary_key=True)
    StationName=models.CharField(max_length=256,default="no_name")
    Wifi=models.IntegerField()
    NameSoundex=models.CharField(max_length=120)
    Score=models.IntegerField(blank=True,default=0)

    def __str__(self) -> str:
        return self.StationCode
class RouteStations(models.Model):
    stnCode=models.CharField(max_length=10)
    stnName=models.CharField(max_length=180)
    longitude=models.FloatField()
    latitude=models.FloatField()
    isHalt=models.IntegerField()
    distanceFromOrigin=models.IntegerField()
    daySinceDepart=models.IntegerField()
    schedulledArrival=models.CharField()
    schedulledDepart=models.CharField()
    slNo=models.IntegerField()
    # isOrigin=models.IntegerField()
    # isDestination=models.IntegerField()
    platformNo=models.IntegerField()

    def __str__(self) -> str:
        return self.stnCode

class TrainFullInfo(models.Model):
    trainCode = models.CharField(max_length=15,primary_key=True,default='')
    trainName = models.CharField(max_length=256,default='')
    trName=models.CharField(default='')
    #srcStation = models.ForeignKey(Stations,on_delete=models.CASCADE,related_name='srcStation')
    srcStation = models.JSONField(default='{}')
    #destStation = models.ForeignKey(Stations,on_delete=models.CASCADE,related_name='destStation')
    destStation=models.JSONField(default='{}')
    distance=models.IntegerField(default=0)
    duration=models.CharField(max_length=10,default='')
    halts=models.IntegerField(default=0)
    trainId=models.IntegerField(default=0)
    depTimeFromSrc=models.CharField(max_length=10,default='')
    arrTimeAtDest=models.CharField(max_length=10,default='')
    avgSpeed=models.CharField(max_length=10,default='')
    depDays=ArrayField(models.CharField(max_length=4,blank=True,default=''),size=7,default=[''])
    #route = ArrayField(RouteStations())
    trname_telgu=models.CharField(default='')
    trname_hindi=models.CharField(default='')
    trname_bengali=models.CharField(default='')
    trname_tamil=models.CharField(default='')
    trname_kannada=models.CharField(default='')
    trname_malyalam=models.CharField(default='')
    trname_marathi=models.CharField(default='')
    trname_gujrati=models.CharField(default='')
    coach=ArrayField(models.CharField(default=''))
    reversal=ArrayField(models.CharField(default='',blank=True),blank=True)
    trainType=models.CharField(default='')
    inaugural=models.CharField(default='')
    wiki=models.CharField(default='')
    sound=models.CharField(default='')
    rake=models.CharField(default='')
    trainRunsOn=models.CharField(default='')
    haltsList=ArrayField(models.CharField(default=''),blank=True)
    arrDayTimeList=ArrayField(ArrayField(models.CharField(),size=2,blank=True),blank=True,default=[''])
    depDayTimeList=ArrayField(ArrayField(models.CharField(),size=2,blank=True),blank=True,default=[''])
    haltsDistList=ArrayField(models.IntegerField(default=0,blank=True),blank=True,default=[0])
    platformList=ArrayField(models.CharField(default=0,blank=True,max_length=20),blank=True,default=[''])
    def __str__(self) -> str:
        return self.trainCode
class TrainRoute(models.Model):
    '''Train Travel Route'''
    trainName=models.CharField(default='')
    trainNameOtherLang=models.JSONField()
    trainCode=models.CharField(primary_key=True,default='')
    srcStn=models.JSONField()
    destStn=models.JSONField()
    duration=models.CharField(default='')
    runsOn=models.CharField(default='')
    route=models.JSONField()
    halts=models.IntegerField()
    

class RouteInfo1(models.Model):
    trainCode = models.CharField(max_length=25,primary_key=True)
    route = models.JSONField()