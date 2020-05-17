full=input()
n=int(input())
forms=list(input().split())
amhos=[]
i=0
for form in forms:
    if form=="int": temp=8
    elif form=="char": temp=2
    elif form=="long_long": temp=16
    amhos.append(full[i:i+temp])
    i+=temp

for amho in amhos:
    print(int(amho, 16), end=" ")
