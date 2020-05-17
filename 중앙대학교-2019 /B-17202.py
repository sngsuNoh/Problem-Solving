num1=list(input())
num2=list(input())
answer=[]
for i in range(len(num1)):
    answer.append(num1[i])
    answer.append(num2[i])
while len(answer)>2:
    temp=[]
    for i in range(len(answer)-1):
        temp.append(str(int(answer[i])+int(answer[i+1]))[-1])
    answer=temp
print(answer[0]+answer[1])
    
