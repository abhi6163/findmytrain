# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
import json


halts='[AZA,NJP,SEL,KEB]'
allStations='AZA,MRZA,CGON,BMGN,BOKO,SNCA,DPRA,RGJI,AMGA,DDNI,KRNI,GLPT,PNVT,JPZ,AYU,MZQ,NBQ,NBQY,DTX,BSGN,SLKX,KOJ,FKM,CROA,GOGH,SRPB,JOQ,KAMG,SMTA,NOQ,NBS,NCB,PQZ,SJRR,GDX,GUZ,FLK,SXX,KLGR,DQG,ATM,BYXA,NMX,NQH,YLSC,JPE,RQJ,BLK,ABFC,NJP,RNI,CAT,DMZ,TMH,MXJ,AUB,GEOR,GIL,PJP,KNE,THED,HWR,KKA,SJKL,DLK,TETA,AHL,SUD,SJGM,BOE,MFA,BWPB,AZR,KMPH,KWE,BAHN,KDPR,HCR,MQG,BKRD,MFZ,SM,SRPU,KMRJ,MBC,EKI,ADF,OMLF,MLDT,GZM,JMQ,KTJ,CMX,NFK,TDLE,BDBS,BDAG,BDLC,GMAN,KLP,TBB,PKR,NGF,RJG,BSBR,MRR,CTR,NHT,SDLE,RPH,TPF,MLV,GHLE,SNT,BSLE,AMP,KPLE,PNE,BHP,BDH,PCQ,GKH,NRX,BPS,JTL,KAN,TIT,BWN,GRP,SKG,PRAE,CHC,MSAE,NBAE,JRAE,JPQ,GRAE,HIH,CRAE,SHBC,DNHL,BMAE,PBZ,CDAE,MDSE,KQU,BLAE,MBE,BRPA,BPAE,JOX,GBRA,DKAE,CCLW,BTNG,BALT,BKNM,MRFO,ADL,SEL,ABB,NALR,BVA,CGA,FLR,ULB,BSBP,KGY,BZN,GGTA,DTE,KIG,MCA,NDGJ,BOP,NPMR,PKEO,PKU,KHAI,HAUR,RDU,DUAN,BCK,SMCK,MPD,JPR,KGP,NPTY,KKQ,KSO,SUA,BNB,JGM,KATB,GII,KNM,CKU,KKPR,DVM,CHGA,GTS,GUD,RHE,ASB,GVDP,SLJR,TATA,ADTP,GMH,BRBS,SINI,MMV,RKSN,BRM,CKP,LPH,SWR,TUX,GOL,MXW,DRWN,PST,GHAA,MOU,JRA,BUL,BZR,BNDE,BNDM,KCAB,ROU,PPO,KLG,KXN,GP,SXN,SOGR,GPH,TGM,BMB,DIH,BEH,PNPL,DTV,JSG,IB,BRJN,LKCB,BPH,HGR,DAO,IBH1,JMG,KRL,RIG,KDTR,BEF,SPBC,ROB,KHS,JDI,SKT,JDDA,IBH3,BUA,SGRD,SRGD,CPH,IBH5,NIA,KPNA,AKT,LCA,KTSH,JRMG,GTW,BSP,DPH,CHBT,BYL,DGS,IBHH,NPI,IBHG,BYT,IBHF,HNEO,HN,IBHE,TLD,BKTH,BKTW,IBHD,SLH,IBHC,MDH,URK,WRC,R,SRWN,SZB,KMI,CABN,DCAB,DBEC,HCAB,BIA,BPHB,BQR,DLCB,DURG,RSM,MUP,PMS,RJN,BAKL,MUA,JTR,DGG,PJB,BTL,DKS,SKS,DNL,AGN,GDM,G,GJ,KWN,TRO,MNU,TMR,KOKA,BRD,KHAT,RRL,TAR,CHCR,SAL,KNHN,KP,KAV,NGP,AJNI,KRI,GMG,BTBR,BOK,SNI,TGP,SLOR,VADR,SEGM,WR,DAE,KAOT,PLO,TLN,DMN,DIP,CND,MLR,TMT,BD,TKI,KUM,MNDA,MANA,MZR,KTP,BGN,YAD,AK,GAO,PS,NGZ,SEG,JM,NN,KJL,BIS,WADO,MKU,KMKD,KLHD,BDWD,ACG,VNA,BSCN,BSL,BDI,JL,PLD,CHLK,DXG,BHNE,TKHE,AN,BRTK,PDP,BEW,NDN,HOL,SNK,SNSL,VKH,DDE,RNL,TISI,CUE,NDB,DWD,BAWD,KBH,KHTG,CPD,KFF,NWU,BBAI,LKKD,USD,DSD,KKRD,VYA,LTV,KRAI,MID,MGRL,TBV,BIY,GGAR,BGMR,CHM,BHET,SCH,MRL,NVS,GNST,HXR,VDH,ACL,AML,BIM,JRS,DGI,BL,ATUL,PAD,UVD,BAGD,VAPI,KEB,'
distance=[0,11,23,35,44,52,62,71,82,92,104,113,121,131,146,155,164,166,168,176,183,193,203,214,227,234,245,253,263,273,284,291,301,306,313,321,330,339,344,351,358,366,371,375,378,383,390,399,409,417,424,438,447,455,461,473,481,487,495,504,506,512,518,525,532,541,544,550,554,560,564,569,573,578,581,584,588,595,600,605,610,616,620,625,629,632,638,645,650,658,663,670,679,684,689,692,697,698,700,707,715,719,725,730,737,742,750,758,766,773,780,785,794,801,809,814,823,830,834,842,847,853,859,864,869,873,879,886,893,898,903,906,909,912,916,919,923,926,928,930,932,935,937,941,946,948,950,952,955,959,961,965,967,970,972,975,978,980,983,986,987,989,992,995,997,998,1002,1004,1008,1011,1013,1016,1019,1021,1023,1026,1026,1028,1032,1035,1039,1041,1044,1048,1053,1057,1062,1067,1069,1074,1080,1086,1092,1097,1104,1110,1114,1121,1128,1133,1137,1145,1150,1154,1160,1163,1165,1169,1173,1180,1186,1192,1197,1205,1213,1220,1229,1233,1238,1242,1245,1250,1254,1258,1267,1272,1278,1282,1284,1285,1289,1293,1299,1304,1311,1317,1322,1325,1331,1338,1345,1350,1355,1359,1366,1372,1375,1378,1381,1391,1396,1400,1405,1412,1419,1425,1432,1664,1897,1903,1908,1915,1922,1923,1929,1935,1936,1941,1945,1950,1955,1961,1963,1966,1971,1977,1982,1986,1989,1993,1999,2003,2005,2011,2016,2022,2027,2028,2032,2037,2041,2042,2046,2048,2051,2057,2063,2064,2066,2068,2070,2075,2077,2079,2081,2082,2085,2089,2092,2095,2096,2102,2108,2113,2119,2127,2133,2138,2143,2148,2154,2160,2168,2173,2179,2187,2196,2207,2213,2218,2226,2233,2241,2247,2254,2261,2265,2270,2275,2280,2284,2289,2294,2296,2303,2308,2315,2321,2329,2335,2343,2349,2352,2354,2364,2371,2376,2384,2391,2399,2404,2414,2419,2426,2432,2438,2444,2449,2458,2466,2472,2481,2486,2496,2502,2508,2514,2523,2533,2539,2543,2548,2554,2561,2566,2569,2578,2583,2589,2592,2602,2611,2619,2628,2633,2638,2643,2652,2658,2664,2669,2673,2678,2684,2689,2693,2699,2708,2716,2722,2726,2733,2738,2743,2750,2757,2762,2770,2778,2782,2787,2791,2793,2801,2807,2809,2813,2817,2819,2824,2829,2833,2837,2845,2849,2854,2860,2863,2864,2867,2870,2873,2877,2880,2884,2891,2896,2899,2903,2906,2911,2916]
arrTime='[-,1 21:45,1 16:15,3 15:00]'
depTime='[0 14:00,1 01:45,1 20:15,3 00:00]'
pf='[[0,0,0,0]]'
stationsArray=allStations.split(',')
haltsArray=halts.replace('[','').replace(']','').split(',')
arrTimeArray=arrTime.replace('[','').replace(']','').split(',')
depTimeArray=depTime.replace('[','').replace(']','').split(',')
pfArray=pf.replace('[','').replace(']','').split(',')
print(arrTimeArray)
print(depTimeArray)
print(pfArray)
arr=[]
for index,time in enumerate(arrTimeArray):
    day=''
    t=''
    if index==0:
        day='1'
        t='Start'
    elif index==len(arrTimeArray):
        t='end'
        temp=time.split(' ')
        day=str(int(temp[0])+1)
    else:
        temp=time.split(' ')
        day=str(int(temp[0])+1)
        t=temp[1]
    tempArr=[day,t]
    arr.append(tempArr)
wholeRoute={}

#print(arr)
noHalts=[]
i=0
for station in stationsArray:
    #print(i)
    stn={}
    if len(haltsArray)<1 or i>len(haltsArray)-1:
        break
    halt=haltsArray[i]
    if halt==station:
        noHalts=[]
        stn.update({'StationName':halt,'arrivalTime':arr[i][1],'Day':arr[i][0],'subroute':[]})
        
        wholeRoute[halt]=stn
        i=i+1
        #haltsArray.remove(haltsArray[0])
    else:
        noHalts.append(station)
        wholeRoute[haltsArray[i-1]]['subroute']=noHalts
    wholeRoute[halt]=stn
json_object = json.dumps(wholeRoute, indent = 4) 
print(json_object)