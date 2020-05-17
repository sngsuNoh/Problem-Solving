import sys

a,b=map(int, sys.stdin.readline().split()) #get a and b for x^2+2ax+b=0

if a**2-b==0: #one root
    print(-a)

else: #two roots
    small=-a-((a**2-b)**(1/2))
    big=-a+((a**2-b)**(1/2))
    print(int(small),int(big))
