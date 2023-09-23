# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
import codecs
import base64
import hashlib
import random
from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import pad, unpad
from Cryptodome.Random import get_random_bytes
import requests,json
from datetime import datetime



sckey='645fbc1e56e23365f2f3c204ae0899f6'
iv=b'7DC5EB3BB4DB6EA8'
key=b'8EA4DB2CC1EB3DC5'
d='EA3541BC74345DDA'
def trainsBwStations(frm,to,traintype):
    tbs='service=TrainRunningMob&subService=TrainBtwStnJson&stnFrom='+frm+'&stnTo='+to+'&trainType='+traintype
    return MyCrypto.decrypt(MyCrypto.fromHex(my_django_view(tbs)['jsonIn']))
def liveStation(station,withinhrs,to):
    st='service=TrainRunningMob&subService=TrainsAtStationJson&jStation='+station+'&nHr='+withinhrs+'&jToStation='+to
    return MyCrypto.decrypt(MyCrypto.fromHex(my_django_view(st)['jsonIn']))
def trainTypes():
    tt='service=TrainRunningMob&subService=TrainTypeList'
    return MyCrypto.decrypt(MyCrypto.fromHex(my_django_view(tt)['jsonIn']))
def getTrainLiveLocation(trainNo):
    '''jjjj'''
    tt='service=TrainRunningMob&subService=GetTrainInstance&trainNo='+trainNo
    return MyCrypto.decrypt(MyCrypto.fromHex(my_django_view(tt)['jsonIn']))
def getFullRunningOFTrain(trainNo):
    time = datetime.now()
    print(time.strftime("%d-%b-%Y"))
    tt='service=TrainRunningMob&subService=ShowFullRunJson&trainNo='+trainNo+'&jStation=&jDateType=&arrDepFlag=D&startDate='+str(time.strftime("%d-%b-%Y"))
    print(tt)
    return MyCrypto.decrypt(MyCrypto.fromHex(my_django_view(tt)['jsonIn']))
def my_django_view(string):
    url = "https://enquiry.indianrail.gov.in/crisns/AppServAnd"
    meta=MyCrypto.getMeta().upper()
    header = {
    "Content-Type":"application/json",
    "charset":"utf-8",
    "meta"+meta:MyCrypto.getData(meta).upper(),
    "User-Agent":"Dalvik/2.1.0 (Linux; U; Android 11; A50 Build/RQ1A.210105.003)",
    }
    payload = {   
    "jsonIn": MyCrypto.getMD5(string+sckey).upper()+'#'+MyCrypto.toHex(MyCrypto.encrypt(string)).upper()
    }
    result = requests.post(url,  json=payload, headers=header)
    
    if result.status_code == 200:
        return result.json()
    else:
        result={'jsonIn':'No result Found'}
        return result
    
class MyCrypto:
    
    def encrypt(plain_text):
        cipher = AES.new(key, AES.MODE_CBC,iv)
        padtext = pad(plain_text.encode('utf-8'),16)
        text=cipher.encrypt(padtext)
        base64string=codecs.encode(text,'base64')
        base64string=base64string.decode('utf-8').strip()
        return base64string
    def decrypt(base64string:str):
        cipher = AES.new(key, AES.MODE_CBC,iv)
        base64string=base64string.encode('utf-8')
        decodedString=base64.b64decode(base64string)
        unpaddedtext=unpad(cipher.decrypt(decodedString),16)
        return unpaddedtext.decode('utf-8')
    def toHex(string):
        return codecs.encode(string.encode('utf-8'),'hex').decode('utf-8')
    def fromHex(hex):
        return codecs.decode(hex,'hex').decode('utf-8')
    def getMeta():
        meta=''
        meta=codecs.encode(get_random_bytes(16),'hex')[0:16]
        # while len(meta)<16:
        #     meta+=codecs.encode(str(random.random()),'hex')
        return meta.decode('utf-8').upper()
    def getData(string):
        return MyCrypto.getMD5(string+d)

    def getMD5(st):
        digest = hashlib.md5((st).encode())
        return digest.hexdigest()



#teststr='6430384136355152636A2B7345435539465A72522B37364E7358716157656E6F756C52516F4A616951377362446243325A4B4A534B5363426837667A496878564D6B4B34376B31544A4548470A5A576766385A58397238574A484A6333565A33687573467563715A464E743463747145326941426F77367933467934493351417A686339617A567334334B2B62475670323332494D57394F4B0A643353737277664C4F7278512F4551426462633D'
#print(MyCrypto.fromHex(my_django_view()['jsonIn'].encode('utf-8')))
#print(trainsBwStations('ROK','DLI','XXX'))
#print(getTrainLiveLocation('14624'))
#print(getFullRunningOFTrain('14624'))
#print(MyCrypto.decrypt(MyCrypto.fromHex(my_django_view()['jsonIn'])))
#print(MyCrypto.decrypt(MyCrypto.fromHex(teststr.encode('utf-8'))))
# BS = 16
# #pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS) 
# unpad = lambda s : s[0:-ord(s[-1])]
#service=TrainRunningMob&subService=GetTrainInstance&trainNo=19224
#st='service=TrainRunningMob&subService=TrainsAtStationJson&jStation=DLI&nHr=4&jToStation='
#service=TrainRunningMob&subService=ShowFullRunJson&trainNo=19224&jStation=&jDateType=&arrDepFlag=D&startDate=02-Sep-2023
# #instance.update(str.getBytes())
# digest = hashlib.md5((st+sckey).encode())
#print(digest.hexdigest())
# stringBuffer = ''
# MAX_VALUE=bytes(255)
# MIN_VALUE=bytes(0)
# for b in digest:
#     stringBuffer+=(str(int(((b & MAX_VALUE) + MIN_VALUE, 16)))[1:])

#strs='6430384136355152636A2B7345435539465A72522B37364E7358716157656E6F756C52516F4A61695137735058326448774C717566714C744C6F4A6F7A30755451366A745272554C694765630A313053735479706A643951526B556145387236736952504242756950484B4D36374B38413433547A306979374F4C633269397536'
#print(MyCrypto.getData('BA7D3FC16F0F6616'))
# #print(getDecodedText(strs).strip())bytes(key, 'utf-8'),bytes(iv, 'utf-8')
# decrypt_cipher = AES.new(key, AES.MODE_CBC,iv)
# #plain_text = decrypt_cipher.decrypt(base64.b64decode(bytes(getDecodedText(strs).strip(), 'utf-8')))
# padtext = pad(st.encode('utf-8'),16)
# plain_text=decrypt_cipher.encrypt(padtext)
# base64string=codecs.encode(plain_text,'base64')
# base64string=base64string.decode('utf-8').strip().encode('utf-8')
# #print(base64string.decode('utf-8').strip().encode('utf-8'))
# #print(base64.b64decode(base64string).encode('hex').upper())
# #inthex=int(base64string,16)
# #print(codecs.encode(base64.b64decode(base64string),'hex'))
# print(digest.hexdigest().upper()+'#'+codecs.encode(base64string,'hex').decode('utf-8').upper()) 