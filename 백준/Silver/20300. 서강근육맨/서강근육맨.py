import sys
input = sys.stdin.readline

N = int(input())
li = list(map(int, input().split()))
li.sort()

m = 0

if N%2==0:
    for i in range(N//2):
        m = max(li[i]+li[-i-1], m)
    print(m)
else:
    for i in range(N//2):
        m = max(li[i]+li[-i-2], m)
    print(max(m, li[-1]))