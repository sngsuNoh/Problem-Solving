def solution(budgets, M):
    answer=0
    left=0
    right=max(budgets)
    while right>=left:
        mid=(left+right)//2
        temp=0
        for i in budgets:
            if i>mid: temp+=mid
            else: temp+=i
        if temp>M:
            right=mid-1
        else:
            left=mid+1
            answer=mid
    return answer
