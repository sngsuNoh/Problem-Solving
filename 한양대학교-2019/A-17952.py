import sys
semester=int(sys.stdin.readline())
tasks=[]
for s in range(semester):
    tasks.append(list(map(int,sys.stdin.readline().split())))
point=0
left=0
for d,task in enumerate(tasks[::-1]):
    left+=1
    if task[0]:
        if left>=task[2]: point+=task[1]
        left-=task[2]
        if left<0: left=0
        
sys.stdout.write(str(point))
