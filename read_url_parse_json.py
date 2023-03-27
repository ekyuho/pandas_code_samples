import requests
import json

r = requests.get('http://openapi.seoul.go.kr:8088/78554a7352656b793832646856754d/json/bikeList/1/5/')

#print(r.text)
j = r.json()
#print(json.dumps(j,indent=4, ensure_ascii=False))

#print(j['rentBikeStatus']['row'])
for x in j['rentBikeStatus']['row']:
  print(x['stationName'], x['parkingBikeTotCnt'])
