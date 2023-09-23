# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
import codecs
import base64
import hashlib
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

BS = 16
#pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS) 
unpad = lambda s : s[0:-ord(s[-1])]
sckey='645fbc1e56e23365f2f3c204ae0899f6'
iv=b'7DC5EB3BB4DB6EA8'
key=b'8EA4DB2CC1EB3DC5'
st='service=TrainRunningMob&subService=TrainsAtStationJson&jStation=DLI&nHr=4&jToStation='
#instance.update(str.getBytes())
digest = hashlib.md5((st+sckey).encode())
#print(digest.hexdigest())
# stringBuffer = ''
# MAX_VALUE=bytes(255)
# MIN_VALUE=bytes(0)
# for b in digest:
#     stringBuffer+=(str(int(((b & MAX_VALUE) + MIN_VALUE, 16)))[1:])
        
strs='''6430384136355152636A2B7345435539465A72522B37364E7358716157656E6F756C52516F4A616951377469374154
4A4A46636F444162306F3038704B4D38377557626C
36343035703439780A555044685645654E4E4C4F343146386A634C4338314A4E3644516B4B314D486E2B41683546355856565
34E496535326D44546B37'''
def getDecodedText(strs):
    length = len(strs) / 2
    bArr =[]
    i=0
    while i < length: 
        i2 = i * 2;
        bArr.append(int(strs[i2:i2 + 2], 16).to_bytes(2, byteorder='big'))
        i=i+1
    stt=''
    for byte in bArr:
        stt+=codecs.decode(byte)
    return stt
#print(getDecodedText(strs).strip())bytes(key, 'utf-8'),bytes(iv, 'utf-8')
decrypt_cipher = AES.new(key, AES.MODE_CBC,iv)
#plain_text = decrypt_cipher.decrypt(base64.b64decode(bytes(getDecodedText(strs).strip(), 'utf-8')))
padtext = pad(st.encode('utf-8'),16)
plain_text=decrypt_cipher.encrypt(padtext)
base64string=codecs.encode(plain_text,'base64')
base64string=base64string.decode('utf-8').strip().encode('utf-8')
#print(base64string.decode('utf-8').strip().encode('utf-8'))
#print(base64.b64decode(base64string).encode('hex').upper())
#inthex=int(base64string,16)
#print(codecs.encode(base64.b64decode(base64string),'hex'))
print(digest.hexdigest().upper()+'#'+codecs.encode(base64string,'hex').decode('utf-8').upper()) 