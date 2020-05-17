def solution(n, lost, reserve):
    slost=set(lost)-set(reserve)
    sres=set(reserve)-set(lost)
    for i in sres:
        if i-1 in slost:
            slost.remove(i-1)
        elif i+1 in slost:
            slost.remove(i+1)
    return n-len(slost)
