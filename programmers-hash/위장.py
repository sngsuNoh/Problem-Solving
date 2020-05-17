from collections import Counter
def solution(clothes):
    answer = 1
    clothes_list=[]
    for i in clothes:
        clothes_list.append(i[1])
    temp=Counter(clothes_list)
    cate=list(temp.values())
    for i in cate:
        answer*=(i+1)
    return answer-1
