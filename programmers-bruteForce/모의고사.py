from math import ceil
def solution(dap):
    answer=[]
    l=len(dap)
    su1=[1,2,3,4,5]*ceil(l/5)
    su2=[2,1,2,3,2,4,2,5]*ceil(l/8)
    su3=[3,3,1,1,2,2,4,4,5,5]*ceil(l/10)
    a=0
    b=0
    c=0
    for i in range(l):
        if dap[i]==su1[i]: a+=1
        if dap[i]==su2[i]: b+=1
        if dap[i]==su3[i]: c+=1
    if a>=b and a>=c: answer.append(1)
    if b>=c and b>=a: answer.append(2)
    if c>=a and c>=b: answer.append(3)
    return answer
