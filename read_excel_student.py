import pandas as pd 

enrolled = pd.read_excel('수강생.xlsx', sheet_name='졸프',header=None)
#enrolled = enrolled[enrolled.iloc[:,5] == '학생']
enrolled =  enrolled.fillna("")
enrolled

students={}
k=1
for i,r in enrolled.iterrows():
    team=""
    for j,n in r.items():
        if j==0: 
            team=n
            continue
        if j==1:
            #team +=f"{n} /"
            continue
        if n != "":
            x=n.replace(')','').split('(')
            print(k, team, x[1], '/',x[0])
            students[x[1]]=team
            k+=1
            
stu = pd.read_excel('수강생.xlsx', sheet_name='팀to개인')
s1=stu.iloc[:,0]
for i in range(len(s1)):
    print(i, s1[i])
print('--')
for s in students:
    print(s,students[s],s1[students[s]-1])
    
for i,r in stu.iterrows():
    if str(r[3]).strip() in students:
        #print('졸프', r[1],r[2],r[3],r[4])
        s=students[r[3]]
        print(s[0], '/', r[1], '/', r[2], '/', r[3],'/', r[4], '/', r[6], '/', r[7])
    else:
        #print('스타트', r[1],r[2],r[3],r[4])
        pass  
      
      
print("1. 그로쓰 프로젝트팀 명단에 들어있는 학생들")
m=0
for x in students:
    print(students[x]['name'], end=',')
    m+=1
    if m%10 == 0: print()
print('\ntotal ', m, '학생들')
print()

n=0
print("2. 사캠 캡스톤디자인 수강신청 명단 전체")
for i,r in stu.iterrows():
    print(r[4], end=',')
    n+=1
    if n%10 == 0: print()
print('\ntotal ', n, '학생들')
print()

print("3. 그로쓰 프로젝트팀 명단의 구성원들 중 사캠 참여학생 명단에 있는 학생들")
i=0
for x in students:
    if students[x]["continue"]=="yes": 
        print(students[x]['name'], end=',')
        i+=1
        if i%10 == 0: print()
print('\ntotal ', i, '학생들')
print()
j=0
print("4. 그로쓰 구성원들 중 사캠 참여학생 명단에 없는 학생들 (청강)")
for x in students:
    if students[x]["continue"]=="no": 
        print(students[x]['name'], end=',')
        j+=1
        if j%10 == 0: print()
print('\ntotal ', j, '학생들')
print()
k=0
print("5. 스타트팀 구성원")
for i,r in stu.iterrows():
    if not str(r[3]).strip() in students:
        print(r[4], end=',')
        k+=1
        if k%10 == 0: print()
print('\ntotal ', k, '학생들')
      
