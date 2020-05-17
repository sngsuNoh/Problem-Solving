n,bo=map(int,input().split())
nums=[]
for _ in range(n):
    nums.append(int(input()))
key=0
isTrue=False
visit=[False for i in range(n)]
cnt=0
while True:
    if nums[key]==bo:
        cnt+=1
        break
    if visit[nums[key]]==True:
        isTrue=True
        break
    else:
        key=nums[key]
        visit[key]=True
        cnt+=1
if isTrue:
    print(-1)
else:
    print(cnt)
