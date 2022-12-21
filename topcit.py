import pandas as pd 

topcit = pd.read_excel('제 18회 TOPCIT_최종_성적.xlsx', sheet_name='등록접수자')
topcit = topcit[topcit.iloc[:,20] == '출석'][['성명',' 연락처', '총점']]

growth=['홍길동',...]

for index, row in topcit.iterrows():
    if row['성명'] in growth:
        if int(row['총점'])>=400: p=5
        elif int(row['총점'])>=300: p=4
        elif int(row['총점'])>=200: p=3
        elif int(row['총점'])>=100: p=1
        print(index, row['성명'], row[' 연락처'], row['총점'], p)
