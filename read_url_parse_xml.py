# https://freeharmony.tistory.com/64
import requests
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup

r=requests.get('https://www.kma.go.kr/wid/queryDFSRSS.jsp?zone=1141058500')
#soup = BeautifulSoup(r.content, "html.parser")
soup = BeautifulSoup(r.content, features="xml")   #  pip3 install lxml
data=[]
for temp in soup.findAll('temp'):
  print(temp, temp.string)
  data.append(float(temp.string))

fig, ax = plt.subplots()  # Create a figure containing a single axes.
ax.plot(data)
