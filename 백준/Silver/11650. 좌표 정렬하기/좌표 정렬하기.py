import sys
n=int(sys.stdin.readline())
t=[]
for _ in range(n):
    [x,y]=map(int, sys.stdin.readline().split())
    t.append([x,y])
t.sort()
for i in range(n):
    print(t[i][0], t[i][1])