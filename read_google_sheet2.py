import pandas as pd
import numpy as np
import json
import re

sheet_id = "sheet_id______here"
sheet_name = "설문지 응답 시트1".replace(" ", "%20").encode('utf-8')
sheet_url = f'https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}'

df=pd.read_csv(sheet_url,encoding='utf-8')

student=[[2323233,'홍길동'],[2323244,'길창덕'], ...]

for i, r in df.iterrows():
    if i==0:
        k=0
        for x in r.keys():
            print(k,x.replace('\n', ' '))
            k+=1
        print()
        continue
output={}
for i,r in df.iterrows():
    stu=r[2]
    m=re.search(' *(\d{7})(.*)',stu)
    if m:
        hakbun=int(m.group(1))
        name=m.group(2).strip()
        content=r[3]
        output[hakbun]={'name':name,'content':content}
    else:
        print('no match', stu)
        
for e in student:
    if e[0] in output:
        print(f"3,{e[0]},{e[1]},{output[e[0]]['content']}")
    else:
        print(f",{e[0]},{e[1]}")
