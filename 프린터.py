def solution(pri, loc):
    cnt=0
    while True:
        if max(pri)==pri[0]:
            cnt+=1
            pri.remove(pri[0])
            if loc==0: return cnt
            else:
                loc-=1
                if loc==-1: loc=len(pri)-1
        else:
            pri.append(pri.pop(0))
            loc-=1
            if loc==-1: loc=len(pri)-1
