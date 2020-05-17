n,sai=map(int,input().split())
fast=list(map(int,input().split()))
cases=[]
for i in range(sai):
    cases.append(list(map(int,input().split())))
for case in cases:
    temp=0
    for i in range(case[0],case[1]):
        temp+=abs(fast[i-1]-fast[i])
    print(temp)
