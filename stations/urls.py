from django.urls import path
from stations import views

app_name = 'stations'

urlpatterns=[path('stations',views.StationInfoView.as_view(),name='stations'),
             path('trains',views.TrainInfoView.as_view(),name='trains'),
             path('stationsNew',views.StationsNewView.as_view(),name='stations_new'),
             path('route',views.TrainRouteInfo.as_view(),name='route'),
             path('trainsbwstations/',views.TrainsBwStations.as_view(),name='trainsbwstations'),
             path('livestation',views.LiveStationStatus.as_view(),name='livestation'),
             path('trainlivelocation',views.TrainLiveLocation.as_view(),name='trainlivelocation'),
             path('fullrunningoftrain',views.FullRunningOfTrain.as_view(),name='trainlivelocation'),
             path('traintypes',views.TrainType.as_view(),name='trainlivelocation'),
             path('wimtlivestation',views.WimtLiveStation.as_view(),name='wimtlivestation'),
             path('wimttrainlivestatus',views.WimtTrainLiveStatus.as_view(),name='wimttraimlivestatus'),
             ]