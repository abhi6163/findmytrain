import uuid
import zlib
import requests
from datetime import datetime

user='e6a55fb9579c457c9368301cf05cca66'
appversion='7.1.5.622738300'
def getWIMTTrainLiveLocation(trainNo,time,frm,to):
    """get live location of train from wimt"""
    print('running')
    today=datetime.strptime(datetime.now().strftime("%d-%m-%Y"),"%d-%m-%Y")
    date=time.strftime("%d-%m-%Y")
    day=today-time
    daydiff=day.days+1
    
    qid=getQid()
    trainno=trainNo
    frm=str.upper(frm)
    to=str.upper(to)
    
    dayfrom=str(daydiff)
    wid=getTrainLiveLocationWid(user,appversion,qid,trainno,frm,to,date,dayfrom)
    print(wid)
    apiURL=getLiveTrainLocationURL(user,appversion,qid,trainno,frm,to,date,dayfrom,wid)
    print(apiURL)
    return(requests.get(apiURL).json())
def getQid():
    '''gettin random qid'''
    return str(uuid.uuid4()).replace('-','')
def getTrainLiveLocationWid(user,appversion,qid,trainno,frm,to,date,dayfrom):
    '''getting wid'''
    string=user+appversion+qid+trainno+frm+to+date+dayfrom
    print(string)
    return str(zlib.adler32(str.encode(string)))
def getLiveTrainLocationURL(user,appversion,qid,trainno,frm,to,date,dayfrom,wid):
    url='https://whereismytrain.in/cache/live_status?date='+date+'&appVersion='+appversion+'&cellinfo=310_260_-1_-1&qid='+qid+'&from_day='+dayfrom+'&wid='+wid+'&train_no='+trainno+'&from='+frm+'&to='+to+'&lang=en&user='+user+'&sb_version=0&flow=regularPermission'
    return url
def getLiveStationStatusURL(appversion,wid,stationCode):
    '''Live Station Status from whereismytrain'''
    url='https://whereismytrain.in/cache/live_station?appVersion='+appversion+'&wid='+wid+'&cellinfo=310_260_-1_-1&hrs=8&station_code='+stationCode+'&lang=en&user='+user+'&sb_version=0&qid='+getQid()
    return url

def getLiveStationStatusWid(stationCode):
    '''Wid for live station status'''
    string=user+appversion+getQid()+stationCode+'8'
    print(string)
    return str(zlib.adler32(str.encode(string)))
def getLiveStationStatus(stationCode):
    stationCode=str.upper(stationCode)
    wid=getLiveStationStatusWid(stationCode)
    url=getLiveStationStatusURL(appversion,wid,stationCode)
    print(url)
    return(requests.get(url).json())
    