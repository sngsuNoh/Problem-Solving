import sys
height, mul=map(int, sys.stdin.readline().split())
temp,result=1,0
for _ in range(height):
    temp*=mul
    temp%=1000000007
    result+=int(sys.stdin.readline())*temp
    result%=1000000007
sys.stdout.write(str(result))
