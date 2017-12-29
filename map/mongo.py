import pymongo
import pandas as pd

def locationJson():
    url = "mongodb://10.1.11.172:27017,10.1.11.173:27017,10.1.11.174:27017/cwb?replicaSet=LLTRS01"
    client = pymongo.MongoClient()
    db =client.rop
    col = db.air_quality_stn
    cursor =col.find()
    df =pd.DataFrame(list(cursor))
    df=df[["SiteName","TWD97Lon","TWD97Lat"]]
    df =df.T
    return df.to_json()

def gasInfoApi(stn):
    url = "mongodb://10.1.11.172:27017,10.1.11.173:27017,10.1.11.174:27017/cwb?replicaSet=LLTRS01"
    client = pymongo.MongoClient()
    db =client.rop
    col = db.epa
    cursor = col.find({"stn":stn})
    df = pd.DataFrame(list(cursor))
    df=df.T
    #print(df.tail())
    return df.to_json(default_handler=str)

def gasInfoApiByDay(stn,date,):
    url = "mongodb://10.1.11.172:27017,10.1.11.173:27017,10.1.11.174:27017/cwb?replicaSet=LLTRS01"
    client = pymongo.MongoClient()
    db =client.rop
    col = db.epa
    cursor = col.find({"stn":stn,"date":date})
    df = pd.DataFrame(list(cursor))
    df=df.T
    #print(df.tail())
    return df.to_json(default_handler=str)

def sumGas(startDate,endDate,stn):
    #url = "mongodb://10.1.11.172:27017,10.1.11.173:27017,10.1.11.174:27017/cwd?replicaSet=LLTRS01"
    client = pymongo.MongoClient()
    db =client.rop
    col = db.epa
    pipeline=[
        {"$match": {"DT": {"$gte": startDate,"$lte":endDate},"stn":stn}},
        {"$group": {"_id": "null", "PM2dot5": {"$sum": "$PM2dot5"},"CH4": {"$sum": "$CH4"}, "CO": {"$sum": "$CO"},
            "HH": {"$sum": "$HH"},"NMHC": {"$sum": "$NMHC"},"NO": {"$sum": "$NO"},"NO2": {"$sum": "$NO2"},
                    "NOx": {"$sum": "$NOx"},"O3": {"$sum": "$O3"},"PM10": {"$sum": "$PM10"},"SO2": {"$sum": "$SO2"},
                    "RH": {"$sum": "$RH"},"THC": {"$sum": "$THC"},"UVB": {"$sum": "$UVB"},

                    }}
    ]
    cursor =col.aggregate(pipeline)
    df =pd.DataFrame(list(cursor))
    df= df.T
    return df.to_json()

