import urllib.request as request
import json
import pandas as pd
scr = 'https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json'
with request.urlopen(scr) as response:
    data = json.load(response)

jsonObj = data['result']['results']
jsonDF = pd.DataFrame(jsonObj, columns=jsonObj[0])
choiceDay = '2014/12/31'
dataTime = jsonDF[(jsonDF['xpostDate'] > choiceDay)]
dataTime = dataTime.reset_index(drop=True)                   # index照順序排列

# 抓取作業要的資料
df = pd.DataFrame(dataTime, columns = ['stitle','address','longitude','latitude','file'])
df['address'] = df['address'].str.extract(pat = '(..區)')
df[['longitude','latitude']] = df[['longitude','latitude']].astype('float')
df = df.round(4)
df['file'] = df['file'].str.extract(pat = '(https.*?(jpg|JPG))')[0]   # + : 一次或多次， +? : 停止貪婪，碰到後面指定字串/符號後停止

df.to_csv('week-3_1.csv', header=0, index=0)