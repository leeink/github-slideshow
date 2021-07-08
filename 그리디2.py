import sys

N,M,K=map(int,(sys.stdin.readline().rstrip().split()))
natural=list(map(int,(sys.stdin.readline().rstrip().split())))

natural.sort()
first=natural[N-1]
second=natural[N-2]
result=0

count=int(M/(K+1))*K
count+=M%(K+1)
