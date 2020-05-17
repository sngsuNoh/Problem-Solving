def solution(heights):
    answer = [0]
    for i in range(1,len(heights)):
        j=i-1
        while j>=0:
            if heights[j]>heights[i]:
                answer.append(j+1)
                break
            j-=1
        if j==-1: answer.append(0)
        
    return answer
