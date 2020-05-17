import sys

n,t=map(int, sys.stdin.readline().split())

nam=(t%(4*n-2))

if nam>2*n: nam=4*n-nam
sys.stdout.write(str(nam))
