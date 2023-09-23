from django.urls import path
from stations import views

app_name = 'stations'

urlpatterns=[path('stations',views.StationInfoView.as_view(),name='stations'),
             path('trains',views.TrainInfoView.as_view(),name='trains'),
             path('stationsNew',views.StationsNewView.as_view(),name='stations_new'),
             path('route',views.TrainRouteInfo.as_view(),name='route'),
             path('trainsbwstations/from=<frm>&to=<to>',views.TrainsBwStations.as_view(),name='trainsbwstations'),
             ]