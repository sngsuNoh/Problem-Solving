def solution(citations):
    citations.sort()
    answer=0
    for h in range(citations[-1]+1):
        temp=0
        for i in citations:
            if i>=h: temp+=1
        if temp>=h and h>=answer: answer=h
    return answer
