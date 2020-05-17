def solution(length, weight, truck):
    answer = 1
    ing=[]
    cnts=[]
    while True:
        if truck==[] and ing==[]: break
        if truck!=[]:
            if truck[0]+sum(ing)<=weight:
                ing.append(truck[0])
                truck.remove(truck[0])
                cnts.append(length)
        for i in range(len(cnts)):
            cnts[i]-=1
            if cnts[i]==0: ing.remove(ing[0])
                
        answer+=1
    return answer
