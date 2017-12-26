import pymongo
import pandas as pd

def locationJson():
    url = "mongodb://10.1.11.172:27017,10.1.11.173:27017,10.1.11.174:27017/cwb?replicaSet=LLTRS01"
    client = pymongo.MongoClient(url)
    db =client.cwb
    col = db.air_quality_stn
    cursor =col.find()
    df =pd.DataFrame(list(cursor))
    df=df[["SiteName","TWD97Lon","TWD97Lat"]]
    df =df.T
    return df.to_json()

def gasInfoApi(stn):
    url = "mongodb://10.1.11.172:27017,10.1.11.173:27017,10.1.11.174:27017/cwb?replicaSet=LLTRS01"
    client = pymongo.MongoClient(url)
    db =client.cwb
    col = db.epa
    cursor = col.find({"stn":stn})
    df = pd.DataFrame(list(cursor))
    df=df.T
    #print(df.tail())
    return df.to_json(default_handler=str)

def gasInfoApiByDay(stn,date,):
    url = "mongodb://10.1.11.172:27017,10.1.11.173:27017,10.1.11.174:27017/cwb?replicaSet=LLTRS01"
    client = pymongo.MongoClient(url)
    db =client.cwb
    col = db.epa
    cursor = col.find({"stn":stn,"date":date})
    df = pd.DataFrame(list(cursor))
    df=df.T
    #print(df.tail())
    return df.to_json(default_handler=str)



