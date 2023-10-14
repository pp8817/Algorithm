import sys
input = lambda: sys.stdin.readline().rstrip()
import math

M, N = map(int, input().split())
for i in range(max(2,M), N+1):
    cou = 0
    if i <=3:
        print(i)
    for j in range(2, max(3,int(math.sqrt(i)))+1):
        if i%j==0:
            cou = 1
            break
    if cou != 1:
        print(i)