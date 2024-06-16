from rest_framework.views import APIView
from stations.serializers import StationsSerializer, TrainFullInfoSerializer,TrainInfoSerializer,StationsNewSerializer,TrainRouteSerializer
from rest_framework import permissions
from stations.models import Stations
from stations.models import RouteInfo1
from stations.models import TrainFullInfo, StationsNew,TrainInfo,TrainRoute
from rest_framework.response import Response
from rest_framework import status,generics
import MyCrypto
import json
import ast
import os
import WIMT
from findmytrain.settings import BASE_DIR
from django.core import serializers
from django.forms.models import model_to_dict
from rest_framework import filters
from django_filters import FilterSet
from rest_framework.exceptions import APIException
from stations.filters import CustomSearchFilter,FooFilter
from datetime import datetime
import math

    
class StationsNewView(generics.ListAPIView):
    '''About Stations'''
    queryset = StationsNew.objects.all()
    serializer_class = StationsNewSerializer
    filter_backends = [filters.SearchFilter]
    ordering_fields = ['StationCode']
    search_fields = ['^StationCode', '^StationName']
    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.filter_queryset(self.get_queryset())
        serializer = StationsNewSerializer(queryset, many=True)
        return Response(serializer.data[:20],status=status.HTTP_200_OK)
    def filter_queryset(self, queryset):
        """
        Given a queryset, filter it with whichever filter backend is in use.
        You are unlikely to want to override this method, although you may need
        to call it either from a list view, or from a custom `get_object`
        method if you want to apply the configured filtering backend to the
        default queryset.
        """
        for backend in list(self.filter_backends):
            queryset = backend().filter_queryset(self.request, queryset, self)
        return queryset
class TrainInfoView(generics.ListAPIView):
    '''About Train'''
    
    queryset = TrainInfo.objects.all()
    serializer_class = TrainInfoSerializer
    filter_backends = [filters.SearchFilter]
    ordering_fields = ['trainCode']
    search_fields = ['^trainCode', '^trName']
    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.filter_queryset(self.get_queryset())
        serializer = TrainInfoSerializer(queryset, many=True)
        return Response(serializer.data[:20],status=status.HTTP_200_OK)
    def filter_queryset(self, queryset):
        """
        Given a queryset, filter it with whichever filter backend is in use.
        You are unlikely to want to override this method, although you may need
        to call it either from a list view, or from a custom `get_object`
        method if you want to apply the configured filtering backend to the
        default queryset.
        """
        for backend in list(self.filter_backends):
            queryset = backend().filter_queryset(self.request, queryset, self)
        return queryset
class StationInfoView(generics.ListAPIView):
    """Stations Info"""

    queryset = Stations.objects.all()
    serializer_class = StationsSerializer
    filter_backends = [filters.SearchFilter]
    
    ordering_fields = ['StationCode']
    search_fields = ['^StationCode', '^StationName']
    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.filter_queryset(self.get_queryset())
        serializer = StationsSerializer(queryset, many=True)
        return Response(serializer.data[:20],status=status.HTTP_200_OK)
    def filter_queryset(self, queryset):
        """
        Given a queryset, filter it with whichever filter backend is in use.
        You are unlikely to want to override this method, although you may need
        to call it either from a list view, or from a custom `get_object`
        method if you want to apply the configured filtering backend to the
        default queryset.
        """
        for backend in list(self.filter_backends):
            queryset = backend().filter_queryset(self.request, queryset, self)
        return queryset
        

class TrainFullInfoView(generics.ListAPIView):
    """Trains Full Info"""
    
    queryset = TrainFullInfo.objects.all()
    serializer_class = TrainFullInfoSerializer
    filter_backends = [filters.SearchFilter]
    
    ordering_fields = ['trainCode']
    search_fields = ['^trainCode', '^trainName']
    def filter_queryset(self, queryset):
        """
        Given a queryset, filter it with whichever filter backend is in use.
        You are unlikely to want to override this method, although you may need
        to call it either from a list view, or from a custom `get_object`
        method if you want to apply the configured filtering backend to the
        default queryset.
        """
        for backend in list(self.filter_backends):
            queryset = backend().filter_queryset(self.request, queryset, self)
        return queryset
    
    def list(self, request):
        """Getting Stations Info"""
        
        queryset = self.filter_queryset(self.get_queryset())
        serializer = TrainFullInfoSerializer(queryset,many=True)
        return Response(serializer.data[:20],status=status.HTTP_200_OK)
    
class TrainRouteInfo(generics.ListAPIView):
    '''Train Route Info'''
    # json_data = open(os.path.join(BASE_DIR,'route2.json'))   
    # route = json.load(json_data)
    # subrout=route[0]
    # subdist=route[1]
    # wholeRoute={}
    # def getStationInfo(trainCode,stcode,index,isHalt,distance):
        
        
    #     train=TrainInfo.objects.get(pk=trainCode)
    #     dest=StationsNew()
    #     try :
    #         dest=StationsNew.objects.get(pk=stcode)
    #     except:
    #         print(stcode,trainCode)
    #         return
    #     print(index,trainCode)
    #     if isHalt:
            
    #         destst={'stName':dest.stationName,'stCode':stcode,'dist':distance,'lat':dest.latitude,'long':dest.longitude,'wifi':dest.wifi,'isHalt':isHalt,'schArrival':train.arrDayTimeList[index][1],'schDeparture':train.depDayTimeList[index][1],'day':train.arrDayTimeList[index][0],'platform':train.platformList[index],'stName_telgu':dest.stname_te,'stName_hindi':dest.stname_hi,'stName_bengali':dest.stname_bn,'stName_tamil':dest.stname_ta,'stName_gujarati':dest.stname_gu,'stName_kannada':dest.stname_kn,'stName_malyalam':dest.stname_ml,'stName_marathi':dest.stname_mr}
    #     else:
    #         destst={'stName':dest.stationName,'stCode':stcode,'dist':distance,'lat':dest.latitude,'long':dest.longitude,'wifi':dest.wifi,'isHalt':isHalt,'stName_telgu':dest.stname_te,'stName_hindi':dest.stname_hi,'stName_bengali':dest.stname_bn,'stName_tamil':dest.stname_ta,'stName_gujarati':dest.stname_gu,'stName_kannada':dest.stname_kn,'stName_malyalam':dest.stname_ml,'stName_marathi':dest.stname_mr}
    #     return destst
    # trains=TrainInfo.objects.all()
    
    # for train in trains:
    #     trainName=train.trName
    #     trOthLang={'telgu':train.trname_telgu,'hindi':train.trname_hindi,'bengali':train.trname_bengali,'tamil':train.trname_tamil,'kannada':train.trname_kannada,'malyalam':train.trname_malyalam,'marathi':train.trname_marathi,'gujarati':train.trname_gujrati}
    #     #print(json.dumps(trOthLang, ensure_ascii=False))
    #     trainNameOtherLang=trOthLang
    #     trainCode=train.trainCode
    #     srcstcode=train.srcStation['stationCode']
    #     src=StationsNew.objects.get(pk=srcstcode)
    #     srcst={'stName':src.stationName,'stCode':srcstcode,'dist':train.haltsDistList[0],'lat':src.latitude,'long':src.longitude,'wifi':src.wifi,'schArrival':train.arrDayTimeList[0][1],'schDeparture':train.depTimeFromSrc,'day':train.arrDayTimeList[0][0],'platform':train.platformList[0],'stName_telgu':src.stname_te,'stName_hindi':src.stname_hi,'stName_bengali':src.stname_bn,'stName_tamil':src.stname_ta,'stName_gujarati':src.stname_gu,'stName_kannada':src.stname_kn,'stName_malyalam':src.stname_ml,'stName_marathi':src.stname_mr}
    #     srcStn=srcst
    #     deststcode=train.destStation['stationCode']
    #     dest=StationsNew.objects.get(pk=deststcode)
    #     lastHaltIndex=len(train.platformList)-1
    #     destst={'stName':dest.stationName,'stCode':deststcode,'dist':train.haltsDistList[len(train.haltsDistList)-1],'lat':dest.latitude,'long':dest.longitude,'wifi':dest.wifi,'schArrival':train.arrTimeAtDest,'schDeparture':train.depDayTimeList[lastHaltIndex][1],'day':train.arrDayTimeList[lastHaltIndex][0],'platform':train.platformList[lastHaltIndex],'stName_telgu':dest.stname_te,'stName_hindi':dest.stname_hi,'stName_bengali':dest.stname_bn,'stName_tamil':dest.stname_ta,'stName_gujarati':dest.stname_gu,'stName_kannada':dest.stname_kn,'stName_malyalam':dest.stname_ml,'stName_marathi':dest.stname_mr}
    #     destStn=destst
    #     duration=train.duration
    #     runsOn=train.trainRunsOn
        
    #     #print(json.loads(json.dumps(route[0])),trainCode)
    #     rout=json.loads(json.dumps(route[0]))
    #     #routes=route[0].copy()
    #     #print(routes)
        
    #     subrouteList=subrout[trainCode]
    #     subrouteDistance=subdist[trainCode]
    #     stationsArray=subrouteList.split(',')
    #     halts=train.halts
    #     subDistanceArray=subrouteDistance.split(',')
    #     haltsArray=train.haltsList
    #     wholRoute={}
    #     noHalts=[]
    #     i=0
    #     arr=train.arrDayTimeList
    #     dep=train.depDayTimeList

    #     for index,station in enumerate(stationsArray):
    #         #print(i)
    #         stn={}
    #         if len(haltsArray)<1 or i>len(haltsArray)-1:
    #             break
    #         halt=haltsArray[i]
    #         if halt==station:
    #             noHalts=[]
    #             haltDict=getStationInfo(trainCode=trainCode,stcode=halt,index=i,isHalt=True,distance=subDistanceArray[index])
    #             stn.update({'nonStops':[]})
                
    #             wholRoute[i]={**haltDict,**stn}
    #             #print(wholRoute)
    #             i=i+1
    #             #haltsArray.remove(haltsArray[0])
    #         else:
    #             noHalts.append(getStationInfo(trainCode=trainCode,stcode=station,index=index,isHalt=False,distance=subDistanceArray[index]))
    #             wholRoute[i-1].update({'nonStops':noHalts})
    #         #wholRoute[halt]=stn
    #     wholeRoute['route']=wholRoute
    #     route=wholRoute
    #     tr=TrainRoute(trainCode=trainCode,trainName=trainName,trainNameOtherLang=trainNameOtherLang,srcStn=srcStn,destStn=destStn,duration=duration,runsOn=runsOn,halts=halts,route=route)
    #     tr.save()
        
    #json_data2.close()
    queryset = TrainRoute.objects.all()
    serializer_class = TrainRouteSerializer
    filter_backends = [filters.SearchFilter]
    #filter_backends = (DjangoFilterBackend,)
    #filterset_fields= ['trainCode','trainName']
    ordering_fields = ['trainCode']
    search_fields = ['^trainCode', '^trainName']
    def filter_queryset(self, queryset):
        """
        Given a queryset, filter it with whichever filter backend is in use.
        You are unlikely to want to override this method, although you may need
        to call it either from a list view, or from a custom `get_object`
        method if you want to apply the configured filtering backend to the
        default queryset.
        """
        for backend in list(self.filter_backends):
            queryset = backend().filter_queryset(self.request, queryset, self)
        return queryset
    
    def list(self, request):
        """Getting Stations Info"""
        
        queryset = self.filter_queryset(self.get_queryset())
        #queryset = self.filter_backends
        serializer = TrainRouteSerializer(queryset,many=True)
        return Response(serializer.data[:20],status=status.HTTP_200_OK)

class TrainsBwStations(APIView):
    def get(self, request):
        """Getting Stations Info"""
        
        frm=request.GET.get('from')
        if frm is None:
            return Response({'Error':'Please provide ?from= parameter'},status=status.HTTP_400_BAD_REQUEST)
        to=request.GET.get('to')
        if to is None:
            return Response({'Error':'Please provide ?to= parameter'},status=status.HTTP_400_BAD_REQUEST)
        jsonData=MyCrypto.trainsBwStations(frm,to,'XXX')
        dictData=json.loads(jsonData)
        
        return Response(dictData,status=status.HTTP_200_OK)
class LiveStationStatus(APIView):
    def get(self, request):
        """Getting Stations Info"""
        
        stn=request.GET.get('station')
        if stn is None:
            return Response({'Error':'Please provide ?station= parameter'},status=status.HTTP_400_BAD_REQUEST)
        to=request.GET.get('to')
        if to is None:
            to=''
        withinhrs=request.GET.get('withinhrs')
        print(withinhrs)
        type(withinhrs)
        if withinhrs is None:
            withinhrs='2'
        jsonData=MyCrypto.liveStation(stn,str(withinhrs),to)
        dictData=json.loads(jsonData)
        
        return Response(dictData,status=status.HTTP_200_OK)
        
class WimtLiveStation(APIView):
    '''Live Station data from wimt'''
    def get(self,request):
        stn=request.GET.get('station')
        if stn is None:
            return Response({'Error':'Please provide ?station= parameter'},status=status.HTTP_400_BAD_REQUEST)
        
        d=WIMT.getLiveStationStatus(stn)
        return Response(d,status=status.HTTP_200_OK)

class TrainLiveLocation(APIView):
    def get(self, request):
        """Getting Stations Info"""
        
        trn=request.GET.get('trainNo')
        if trn is None:
            return Response({'Error':'Please provide ?trainNo= parameter'},status=status.HTTP_400_BAD_REQUEST)
        
        jsonData=MyCrypto.getTrainLiveLocation(trn)
        dictData=json.loads(jsonData)
        return Response(dictData,status=status.HTTP_200_OK)
class FullRunningOfTrain(APIView):
    def get(self, request):
        """Getting Stations Info"""
        
        trn=request.GET.get('trainNo')
        date=request.GET.get('date')
        
        if trn is None:
            return Response({'Error':'Please provide ?trainNo= parameter'},status=status.HTTP_400_BAD_REQUEST)
        if date is None:
            today=datetime.now().strftime("%d-%m-%Y")
            print('time: '+today)
            date=datetime.strptime(today,"%d-%m-%Y")
        else:
            date=datetime.strptime(date,"%d-%m-%Y")
        train=TrainFullInfo.objects.get(pk=trn)
        jsonData=MyCrypto.getFullRunningOFTrain(trn,date)
        dictData=json.loads(jsonData)
        return Response(dictData,status=status.HTTP_200_OK)
    
class WimtTrainLiveStatus(APIView):
    def get(self,request):
        trn=request.GET.get('trainNo')
        date=request.GET.get('date')
        
        if trn is None:
            return Response({'Error':'Please provide ?trainNo= parameter'},status=status.HTTP_400_BAD_REQUEST)
        if date is None:
            today=datetime.now().strftime("%d-%m-%Y")
            print('time: '+today)
            date=datetime.strptime(today,"%d-%m-%Y")
        else:
            date=datetime.strptime(date,"%d-%m-%Y")
        train=TrainFullInfo.objects.get(pk=trn)
        src=train.srcStation['StationCode']
        dst=train.destStation['StationCode']
        resp=MyCrypto.getWIMTTrainLiveLocation(trn,date,src,dst)
        return Response(resp,status=status.HTTP_200_OK)

class TrainType(APIView):
    def get(self, request):
        jsonData=MyCrypto.trainTypes()
        dictData=json.loads(jsonData)
        return Response(dictData,status=status.HTTP_200_OK)
# class TrainRoutInfo(generics.ListAPIView):
#     """Train Rout By Train Code"""
#     #TrainFullInfo.objects.all().delete()
#     json_data = open(os.path.join(BASE_DIR,'trainsRoute.json'))   
#     trains = json.load(json_data) # deserialises it
#     json_data2 = open(os.path.join(BASE_DIR,'route2.json'))   
#     route = json.load(json_data2) # deserialises it
#     wholeRoute={}
    
#     for train in trains:
#         trainNo=train['trno']
#         trainName=train['trname']
#         trainType=train['traintype']
#         trainRunsOn=train['runson']
#         haltsList=train['stnlist']
#         coach=train['coach']
#         reversal=train['reversal']
#         arrDayTimeList=train['arr']
#         depDayTimeList=train['dep']
#         haltsDistList=train['dist']
#         platformList=train['pf']
#         rake=train['rake']
#         inaugural=train['inaugural']
#         wiki=train['wiki']
#         sound=''
#         trname_telgu=train['trname_te']
#         trname_hindi=train['trname_hi']
#         trname_bengali=train['trname_bn']
#         trname_tamil=train['trname_ta']
#         trname_kannada=train['trname_kn']
#         trname_malyalam=train['trname_ml']
#         trname_marathi=train['trname_mr']
#         trname_gujrati=train['trname_gu']

#         subrouteList=route[0][trainNo]
#         subrouteDistance=route[1][trainNo]
#         wholeRoute={'trainNumber':trainNo,'trainName':trainName,'trainType':trainType,
#                             'runson':trainRunsOn,'coachPosition':coach,'reveral':reversal,
#                             'rake':rake,'inagural':inaugural,'wiki':wiki,'sound':sound,
#                             'trname_telgu':trname_telgu,'trname_hindi':trname_hindi,
#                             'trname_bengali':trname_bengali,'trname_tamil':trname_tamil,
#                             'trname_kannada':trname_kannada,'trname_malyalam':trname_malyalam,
#                             'trname_marathi':trname_marathi,'trname_gujrati':trname_gujrati,'route':{}}
#         arr=[]
#         arrTimeArray=arrDayTimeList.replace('[','').replace(']','').split(',')
#         depTimeArray=depDayTimeList.replace('[','').replace(']','').split(',')
        
#         stationsArray=subrouteList.split(',')
#         haltsArray=haltsList.replace('[','').replace(']','').split(',')
#         for index,time in enumerate(arrTimeArray):
#             day=''
#             t=''
#             if index==0:
#                 day='1'
#                 t='Start'
#             else:
#                 temp=time.split(' ')
#                 print(temp,index)
#                 day=str(int(temp[0])+1)
#                 t=temp[1]
#             tempArr=[day,t]
#             arr.append(tempArr)
#         dep=[]
#         for index,time in enumerate(depTimeArray):
#             day=''
#             t=''
#             if index==len(depDayTimeList):
#                 t='end'
#                 temp=time.split(' ')
#                 day=str(int(temp[0])+1)
#             else:
#                 temp=time.split(' ')
                
#                 day=str(int(temp[0])+1)
#                 t=temp[1]
#             tempArr=[day,t]
#             dep.append(tempArr)
#         i=0
#         wholRoute={}
#         noHalts=[]

#         for station in stationsArray:
#             #print(i)
#             stn={}
#             if len(haltsArray)<1 or i>len(haltsArray)-1:
#                 break
#             halt=haltsArray[i]
#             if halt==station:
#                 noHalts=[]
#                 stn.update({
#                             'StationName':halt,'arrivalTime':arr[i][1],'departureTime':dep[i][1],
#                             'arrDay':arr[i][0],'depDay':dep[i][0],'subroute':[]})
                
#                 wholRoute[halt]=stn
#                 i=i+1
#                 #haltsArray.remove(haltsArray[0])
#             else:
#                 noHalts.append(station)
#                 wholRoute[haltsArray[i-1]]['subroute']=noHalts
#             wholRoute[halt]=stn
#         wholeRoute['route']=wholRoute
#         json_object = json.dumps(wholeRoute, indent = 4) 
#         print(json_object)
#         break
#     serializer_class = RoutInfoSerializer
#     def get_queryset(self):
#         queryset = RouteInfo1.objects.all()
#         code = self.request.query_params.get('trainCode')
#         if code:
#             queryset = queryset.filter(trainCode=code).all()
#         else:
#             raise APIException("train number not supplied or in-correct; Note: link should be like api/route?trainNo=")
#         return queryset
    

# TrainFullInfo.objects.all().delete()
#     json_data = open(os.path.join(BASE_DIR,'trains-1684093672.json'))   
#     data1 = json.load(json_data) # deserialises it
    
#     for d in data1['data']:
#         trains=data1['data'][d]
        
#         try:
#             srcStn=Stations.objects.get(pk=trains['srcStationCode'])
#         except Stations.DoesNotExist:
#             if 'srcStationName' in trains:
#                 srcStn=Stations(Dtude=0.0,Longitude=0.0,StationCode=trains['srcStationCode'],StationName=trains['srcStationName'],Wifi=0,Score=0,NameSoundex='aaa')
#             else:
#                 srcStn=Stations(Latitude=0.0,Longitude=0.0,StationCode=trains['srcStationCode'],StationName='Not Available',Wifi=0,Score=0,NameSoundex='aaa')
        
#         try:
#             dstStn=Stations.objects.get(pk=trains['destStationCode'])
#         except Stations.DoesNotExist:
#             if 'destStationName' in trains:
#                 dstStn=Stations(Latitude=0.0,Longitude=0.0,StationCode=trains['destStationCode'],StationName=trains['destStationName'],Wifi=0,Score=0,NameSoundex='aaa')
#             else:
#                 dstStn=Stations(Latitude=0.0,Longitude=0.0,StationCode=trains['destStationCode'],StationName='Not Available',Wifi=0,Score=0,NameSoundex='aaa')
#         depdays=[trains['departureDays'][0],trains['departureDays'][1],trains['departureDays'][2],trains['departureDays'][3],trains['departureDays'][4],trains['departureDays'][5],trains['departureDays'][6]]
#         train=TrainFullInfo(trainCode=trains['trainCode'],trainName=trains['trainName'],trainId=trains['id'],
#                                 srcStation=model_to_dict(srcStn),
#                                 destStation=model_to_dict(dstStn),
#                                 distance=trains['distance'],duration=trains['duration'],halts=trains['halts'],
#                                 depTimeFromSrc=trains['departureFromSrc'],arrTimeAtDest=trains['arrivalAtDest'],
#                                 avgSpeed=trains['avgSpeed'],depDays=depdays)
#         train.save()
#     json_data.close()

#################################################################################################################################################
# Stations.objects.all().delete()
#     json_data = open(os.path.join(BASE_DIR,'stations.json'))   
#     data1 = json.load(json_data) # deserialises it
#     for station in data1:
#         Wi= 1 if station['Wifi'] == True else 0
#         stn=Stations(Latitude=station['Latitude'],Longitude=station['Longitude'],StationCode=station['StationCode'],
#                         StationName=station['StationName'],Wifi=Wi,Score=station['Score'],NameSoundex=station['NameSoundex'])
            
#         stn.save()
#     json_data.close()
#############################TRAIN FULL INFO DATA FILLING CODE####################################################################################
# TrainFullInfo.objects.all().delete()
#     json_data = open(os.path.join(BASE_DIR,'trains-1684093672.json'))   
#     data1 = json.load(json_data) # deserialises it
#     json_data1 = open(os.path.join(BASE_DIR,'trainsRoute.json'))   
#     trainss = json.load(json_data1) # deserialises it
#     for d in data1['data']:
#         trains=data1['data'][d]
        
#         try:
#             srcStn=Stations.objects.get(pk=trains['srcStationCode'])
#         except Stations.DoesNotExist:
#             if 'srcStationName' in trains:
#                 srcStn=Stations(Latitude=0.0,Longitude=0.0,StationCode=trains['srcStationCode'],StationName=trains['srcStationName'],Wifi=0,Score=0,NameSoundex='aaa')
#             else:
#                 srcStn=Stations(Latitude=0.0,Longitude=0.0,StationCode=trains['srcStationCode'],StationName='Not Available',Wifi=0,Score=0,NameSoundex='aaa')
        
#         try:
#             dstStn=Stations.objects.get(pk=trains['destStationCode'])
#         except Stations.DoesNotExist:
#             if 'destStationName' in trains:
#                 dstStn=Stations(Latitude=0.0,Longitude=0.0,StationCode=trains['destStationCode'],StationName=trains['destStationName'],Wifi=0,Score=0,NameSoundex='aaa')
#             else:
#                 dstStn=Stations(Latitude=0.0,Longitude=0.0,StationCode=trains['destStationCode'],StationName='Not Available',Wifi=0,Score=0,NameSoundex='aaa')
#         depdays=[trains['departureDays'][0],trains['departureDays'][1],trains['departureDays'][2],trains['departureDays'][3],trains['departureDays'][4],trains['departureDays'][5],trains['departureDays'][6]]
#         train=TrainFullInfo(trainCode=trains['trainCode'],trainName=trains['trainName'],trainId=trains['id'],
#                                 srcStation=model_to_dict(srcStn),
#                                 destStation=model_to_dict(dstStn),
#                                 distance=trains['distance'],duration=trains['duration'],halts=trains['halts'],
#                                 depTimeFromSrc=trains['departureFromSrc'],arrTimeAtDest=trains['arrivalAtDest'],
#                                 avgSpeed=trains['avgSpeed'],depDays=depdays,coach=[''],reversal=[''],haltsList=[''],arrDayTimeList=[['']],depDayTimeList=[['']],haltsDistList=[],platformList=[''])
#         train.save()
#     json_data.close()
#     print(trains)
#     for train in trainss:
#         trainNo=train['trno']
#         try:
#             tr=TrainFullInfo.objects.get(pk=trainNo)
#         except TrainFullInfo.DoesNotExist:
#             tr=TrainFullInfo(trainCode=trainNo)
            
#         trainName=train['trname']
#         tr.trName=trainName
#         trainType=train['traintype']
#         tr.trainType=trainType
#         trainRunsOn=train['runson']
#         tr.trainRunsOn=trainRunsOn
#         haltsList=train['stnlist']
#         coach=train['coach']
#         reversal=train['reversal']
#         arrDayTimeList=train['arr']
#         depDayTimeList=train['dep']
#         haltsDistList=train['dist']
#         tr.haltsDistList=haltsDistList
        
#         if len(train['pf']) == 1:
#             platformList=train['pf'][0]
#         else:
#             platformList=train['pf']
#         pf=[]
#         if type(platformList)==str:
#             platforms=platformList[2:-2]
#             pf=platforms.split(',')
#         else:
#             for platform in platformList:
#                 pf.append(str(platform))
#         tr.platformList=pf
#         rake=train['rake']
#         tr.rake=rake
#         inaugural=train['inaugural']
#         tr.inaugural=inaugural
#         wiki=train['wiki']
#         tr.wiki=wiki
#         sound=''
#         trname_telgu=train['trname_te']
#         tr.trname_telgu=trname_telgu
#         trname_hindi=train['trname_hi']
#         tr.trname_hindi=trname_hindi
#         trname_bengali=train['trname_bn']
#         tr.trname_bengali=trname_bengali
#         trname_tamil=train['trname_ta']
#         tr.trname_tamil=trname_tamil
#         trname_kannada=train['trname_kn']
#         tr.trname_kannada=trname_kannada
#         trname_malyalam=train['trname_ml']
#         tr.trname_malyalam=trname_malyalam
#         trname_marathi=train['trname_mr']
#         tr.trname_marathi=trname_marathi
#         trname_gujrati=train['trname_gu']
#         tr.trname_gujrati=trname_gujrati
#         arr=[]
        
#         arrTimeArray=arrDayTimeList.replace('[','').replace(']','').split(',')
#         depTimeArray=depDayTimeList.replace('[','').replace(']','').split(',')
#         haltsArray=haltsList.replace('[','').replace(']','').split(',')
#         tr.haltsList=haltsArray
#         coachArray=coach.replace('[','').replace(']','').split(',')
#         reversalArray=reversal.replace('[','').replace(']','').split(',')
#         tr.coach=coachArray
#         tr.reversal=reversalArray
        

#         for index,time in enumerate(arrTimeArray):
#             day=''
#             t=''
#             if index==0:
#                 day='1'
#                 t='Start'
#             else:
#                 temp=time.split(' ')
#                 #print(temp,index)
#                 day=str(int(temp[0])+1)
#                 t=temp[1]
#             tempArr=[day,t]
#             arr.append(tempArr)
#         dep=[]
#         for index,time in enumerate(depTimeArray):
#             day=''
#             t=''
#             if index==len(depDayTimeList):
#                 t='end'
#                 temp=time.split(' ')
#                 day=str(int(temp[0])+1)
#             else:
#                 temp=time.split(' ')
                
#                 day=str(int(temp[0])+1)
#                 t=temp[1]
#             tempArr=[day,t]
#             dep.append(tempArr)
#         tr.arrDayTimeList=arr
#         tr.depDayTimeList=dep
#         tr.save()
#         json_data1.close()
###################################################################
#### Below code is for station data from json station new##########################################
# StationsNew.objects.all().delete()
#     '''Stations Informations'''
#     json_data = open(os.path.join(BASE_DIR,'stationsNew.json'))   
#     data1 = json.load(json_data) # deserialises it
#     for station in data1:
#         stcode=station['stcode']
#         stname=station['stname']
#         lat=station['lat']
#         long=station['long']
#         city=station['city']
#         state=station['state']
#         if station['postcode']=='':
#             postcode=0
#         else:
#             postcode=station['postcode']
#         wi=station['wifi']
#         wifi=0
#         if wi==1:
#             wifi=1
#         print(wifi,stname)
#         near=station['near']
#         division=station['division']
#         pf=station['pf']
#         category=station['category']
#         score=station['score']
#         neighbours=station['neighbours']
#         wiki=station['wiki']
#         sound=station['sound']
#         stname_te=station['stname_te']
#         stname_hi=station['stname_hi']
#         stname_bn=station['stname_bn']
#         stname_ta=station['stname_ta']
#         stname_kn=station['stname_kn']
#         stname_ml=station['stname_ml']
#         stname_mr=station['stname_mr']
#         stname_gu=station['stname_gu']
#         stn=StationsNew(stationCode=stcode,stationName=stname,latitude=lat,longitude=long,city=city
#                         ,state=state,postCode=postcode,wifi=wifi,near=near,division=division,platforms=pf,
#                         category=category,score=score,neighbours=neighbours,sound=sound,stname_te=stname_te,stname_hi=stname_hi,
#                         stname_bn=stname_bn,stname_ta=stname_ta,stname_gu=stname_gu,stname_kn=stname_kn,stname_ml=stname_ml,stname_mr=stname_mr)
#         stn.save()
#     json_data.close()####

################TRainInFoView Data##############
# TrainInfo.objects.all().delete()
#     json_data = open(os.path.join(BASE_DIR,'trainsRoute.json'))   
#     trains = json.load(json_data) # deserialises it
#     for train in trains:

#         trainNo=train['trno']
#         tr = TrainInfo(trainCode=trainNo)    
#         trainName=train['trname']
#         tr.trName=trainName
#         trainType=train['traintype']
#         tr.trainType=trainType
#         trainRunsOn=train['runson']
#         tr.trainRunsOn=trainRunsOn
#         haltsList=train['stnlist']
#         coach=train['coach']
#         reversal=train['reversal']
#         arrDayTimeList=train['arr']
#         depDayTimeList=train['dep']
#         haltsDistList=train['dist']
#         tr.haltsDistList=haltsDistList
        
#         if len(train['pf']) == 1:
#             platformList=train['pf'][0]
#         else:
#             platformList=train['pf']
#         pf=[]
#         if type(platformList)==str:
#             platforms=platformList[2:-2]
#             pf=platforms.split(',')
#         else:
#             for platform in platformList:
#                 pf.append(str(platform))
#         tr.platformList=pf
#         rake=train['rake']
#         tr.rake=rake
#         inaugural=train['inaugural']
#         tr.inaugural=inaugural
#         wiki=train['wiki']
#         tr.wiki=wiki
#         sound=''
#         trname_telgu=train['trname_te']
#         tr.trname_telgu=trname_telgu
#         trname_hindi=train['trname_hi']
#         tr.trname_hindi=trname_hindi
#         trname_bengali=train['trname_bn']
#         tr.trname_bengali=trname_bengali
#         trname_tamil=train['trname_ta']
#         tr.trname_tamil=trname_tamil
#         trname_kannada=train['trname_kn']
#         tr.trname_kannada=trname_kannada
#         trname_malyalam=train['trname_ml']
#         tr.trname_malyalam=trname_malyalam
#         trname_marathi=train['trname_mr']
#         tr.trname_marathi=trname_marathi
#         trname_gujrati=train['trname_gu']
#         tr.trname_gujrati=trname_gujrati
#         arr=[]
        
#         arrTimeArray=arrDayTimeList.replace('[','').replace(']','').split(',')
#         depTimeArray=depDayTimeList.replace('[','').replace(']','').split(',')
#         haltsArray=haltsList.replace('[','').replace(']','').split(',')
#         tr.haltsList=haltsArray
#         coachArray=coach.replace('[','').replace(']','').split(',')
#         reversalArray=reversal.replace('[','').replace(']','').split(',')
#         tr.coach=coachArray
#         tr.reversal=reversalArray
        

#         for index,time in enumerate(arrTimeArray):
#             day=''
#             t=''
#             if index==0:
#                 day='1'
#                 t='Start'
#             else:
#                 temp=time.split(' ')
#                 #print(temp,index)
#                 day=str(int(temp[0])+1)
#                 t=temp[1]
#             tempArr=[day,t]
#             arr.append(tempArr)
#         dep=[]
#         for index,time in enumerate(depTimeArray):
#             day=''
#             t=''
#             if index==len(depDayTimeList):
#                 t='end'
#                 temp=time.split(' ')
#                 day=str(int(temp[0])+1)
#             else:
#                 temp=time.split(' ')
#                 print(temp[0],trainNo)
#                 day=str(int(temp[0])+1)
#                 t=temp[1]
#             tempArr=[day,t]
#             dep.append(tempArr)
#         tr.arrDayTimeList=arr
#         tr.depDayTimeList=dep
#         ################################################
#         srcst=haltsArray[0]
#         tr.srcStation=model_to_dict(StationsNew.objects.get(pk=srcst))
#         dstst=haltsArray[len(haltsArray)-1]
#         tr.destStation=model_to_dict(StationsNew.objects.get(pk=dstst))
#         depFrmSrc=tr.depDayTimeList[0][1]
#         tr.depTimeFromSrc=depFrmSrc

#         days=int(tr.arrDayTimeList[len(tr.arrDayTimeList)-1][0])
        
#         arrAtDest=tr.arrDayTimeList[len(tr.arrDayTimeList)-1][1]
#         tr.arrTimeAtDest=arrAtDest
        
#         distCovered=tr.haltsDistList[len(tr.haltsDistList)-1]
#         tr.distance=distCovered

#         noOfHalts=len(tr.haltsDistList)-2
#         tr.halts=noOfHalts

#         print('number of halts',noOfHalts)
#         print(trainNo)
#         t1 = datetime.strptime(depFrmSrc, "%H:%M")
#         t2 = datetime.strptime(arrAtDest, "%H:%M")
#         ds1=datetime.strptime('00:00', "%H:%M")
#         d=t2-t1
#         d1=ds1-t1
#         d2=t2-ds1
#         seconds=0
        

#         if days>1:
#             s = d1+d2
#             print(d,'diff',d1,d2)
#             s1 = (days-2)*24*3600
#             #hours=hours+((days-1)*24)
#             seconds=s1+s.seconds
#         else:
#             seconds=d.seconds
#         tr.timeTakeInSec=seconds
#         if seconds>0:
#             dist=int(distCovered)*1000
#             speed= (dist/seconds)*(18/5)
#             hours = seconds // (60*60)
#             seconds %= (60*60)
#             minutes = seconds // 60
#             seconds %= 60
#         else:
#             speed=0
#             hours=0
#             seconds=0
#             minutes=0

#         dur=(hours.__str__()+'h'+minutes.__str__()+'m')
#         #dur=(str(hours)+'h'+str(minutes)+'m')
#         print(dur,type(dur))
#         tr.duration=dur
#         print('time taken ',days,'D',hours,'h',minutes,'m',seconds,'s')
#         print('average speed',math.floor(speed),'km/h')
#         spee=math.floor(speed).__str__()
#         tr.avgSpeed=spee+'km/h'
#         tr.save()
#         json_data.close()
    ################################################
