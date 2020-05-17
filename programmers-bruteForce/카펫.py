def solution(brown, red):
    for i in range(1,red+1):
        j=red//i
        if red%i==0:
            if (i+2)*(j+2)-red==brown: return[j+2,i+2]
