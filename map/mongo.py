import pymongo
import pandas as pd

def locationJson():
    url = "mongodb://10.1.11.172:27017,10.1.11.173:27017,10.1.11.174:27017/cwd?replicaSet=LLTRS01"
    client = pymongo.MongoClient(url)
    db =client.cwb
    col = db.air_quality_stn
    cursor =col.find()
    df =pd.DataFrame(list(cursor))
    df=df[["SiteName","TWD97Lon","TWD97Lat"]]
    return df.to_json()
