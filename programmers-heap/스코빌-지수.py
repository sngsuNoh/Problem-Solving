import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while scoville!=[]:
        if scoville[0]>=K: return answer
        a=heapq.heappop(scoville)
        if scoville!=[]:
            b=heapq.heappop(scoville)
            heapq.heappush(scoville, a+b*2)
        answer+=1
    return -1
