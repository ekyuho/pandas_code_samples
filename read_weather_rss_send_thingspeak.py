# https://freeharmony.tistory.com/64
import requests
import matplotlib.pyplot as plt
import time
from bs4 import BeautifulSoup

while True:
  r=requests.get('https://www.kma.go.kr/wid/queryDFSRSS.jsp?zone=1141058500')
  soup = BeautifulSoup(r.content, "html.parser")
  print(soup.temp.string)

  r=requests.get(f'https://api.thingspeak.com/update?api_key=L60RYNOQ6CARVMRE&field1={soup.temp.string}')
  print(r.text)
  time.sleep(60*10)  # 60초 * 10분
