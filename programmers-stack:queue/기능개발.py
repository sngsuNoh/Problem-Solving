from math import ceil

def solution(progresses, speeds):
    answer = []
    leftli=[]
    for i in range(len(progresses)):
        var=100-progresses[i]
        leftli.append(ceil(var/speeds[i]))
    for i in range(1,len(leftli)):
        if leftli[i]<=leftli[i-1]:
            leftli[i]=leftli[i-1]
    cnt=1
    leftli.append(101)
    for i in range(1,len(leftli)):
        if leftli[i]>leftli[i-1]:
            answer.append(cnt)
            cnt=1
        else:
            cnt+=1
    return answer
