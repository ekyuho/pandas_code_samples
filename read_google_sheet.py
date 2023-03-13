import pandas as pd
import numpy as np
import json
import re

sheet_id = "sheet_id"
sheet_name = "sheet1".replace(" ", "%20").encode('utf-8')
sheet_url = f'https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}'

df=pd.read_csv(sheet_url,encoding='utf-8')
for i, r in df.iterrows():
    if i==0:
        k=0
        for x in r.keys():
            print(k,x.replace('\n', ' '))
            k+=1
        print()
        continue

for i,r in df.iterrows():
  for x in r:
    print(x, r[x])
