from rest_framework import serializers
from stations.models import Stations, RouteInfo1 ,TrainFullInfo, StationsNew,TrainInfo,TrainRoute


class StationsSerializer(serializers.ModelSerializer):
    """Stations Basic Info"""
    class Meta:
        model = Stations
        fields = ['StationName','StationCode','Longitude','Latitude','Wifi','Score','NameSoundex']
class TrainFullInfoSerializer(serializers.ModelSerializer):
    """Serializer for TrainFullInfo Model"""
    class Meta:
        model = TrainFullInfo
        fields = '__all__'
#['trainName','trainCode','trainId','destStation','srcStation','depTimeFromSrc','arrTimeAtDest','duration','distance','avgSpeed','halts','depDays']
class RoutInfoSerializer(serializers.ModelSerializer):
    """Train Rout Info Serializer"""
    class Meta:
        model = RouteInfo1
        fields = '__all__'
class StationsNewSerializer(serializers.ModelSerializer):
    '''Stations Information'''
    class Meta:
        model= StationsNew
        fields = '__all__'

class TrainInfoSerializer(serializers.ModelSerializer):
    '''Train Info'''
    class Meta:
        model=TrainInfo
        fields='__all__'
class TrainRouteSerializer(serializers.ModelSerializer):
    '''TrainRouteSerializer'''
    class Meta:
        model=TrainRoute
        fields='__all__'