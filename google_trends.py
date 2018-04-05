#! coding: utf-8

import requests
import json
import datetime
from pymongo import MongoClient

days = 20

conn= MongoClient()

for day in range(1, days+1):
    dstr = (datetime.date.today()-datetime.timedelta(days = day)).strftime('%Y%m%d')
    url = "https://trends.google.com.tw/trends/hottrends/hotItems"
    data = {
        'ajax': '1',
        'pn':   'p12',
        'htd': dstr,
        'htv': 'l'
    }
    headers = {
        "accept": "*/*",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "en-US,en;q=0.9",
        "content-length": "443",
        "content-type": "application/x-www-form-urlencoded;charset=UTF-8",
        "origin": "https://trends.google.com.tw",
        "referer": "https://trends.google.com.tw/trends/hottrends",
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
        "x-client-data": "CIu2yQEIorbJAQipncoBCKijygEYkqPKAQ==",
        
    }

    resp = requests.post(url, data=data, headers=headers)
    data = resp.json()
    print("[INFO] %s "%data.get('oldestVisibleDate'))
    data['_id'] = data.get("oldestVisibleDate")
    res  = conn.crawler.google_trends.insert(data)
    print(res)

