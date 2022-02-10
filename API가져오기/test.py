import urllib

import requests
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


url = 'http://openapi.seoul.go.kr:8088/sample/json/bikeList/1/5/'
response = urllib.request.urlopen(url)
api = response.read().decode("utf-8")
jsos = json.loads(api)
string = jsos.keys()
dic = {}
for i in string:
    fileName =i
string = jsos[fileName]['row']
for i in string:
    keys = i.items()
    for j in keys:
        dic[j[0]] = j[1]
    docs.append(dic)


#el = helpers.bulk(es,docs)
print("END")