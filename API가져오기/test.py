from bs4 import BeautifulSoup
from xml.etree.ElementTree import fromstring, ElementTree
from elasticsearch import Elasticsearch, helpers
from urllib.request import Request, urlopen
import pandas as pd
from pandas.io.json import json_normalize
import json


es = Elasticsearch(['13.125.221.150:9200'])

docs = []
j = 0

for i in range(3):
    iStart = (i) * 1000 + 1
    iEnd = (i+1) * 1000
    url = 'http://openapi.seoul.go.kr:8088/474a76586572727733385465625659/json/bikeList/' + str(iStart) + '/' + str(iEnd) + '/'
    response = urlopen(url)
    json_api = response.read().decode("utf-8")
    json_file = json.loads(json_api)
    df= json_file['rentBikeStatus']['row']
    for temp in df :
        rackTotCnt = int(temp['rackTotCnt'])
        parkingBikeTotCnt = int(temp['parkingBikeTotCnt'])
        shared = int(temp['shared'])
        stationName = temp['stationName']
        stationLat = temp['stationLatitude']
        stationLon = temp['stationLongitude']
        stationId = temp['stationId']
        n_json ={
            "_index": "seoul_bike",
            "_source" :{
                "stationName" : stationName,
                "rackTotCnt" : rackTotCnt,
                "parkingBikeTotCnt" : parkingBikeTotCnt,
                "stationLat" : stationLat,
                "stationLon" : stationLon,
                "stationId" : stationId
            }
        }
        docs.append(n_json)
el = helpers.bulk(es,docs)
print("END")