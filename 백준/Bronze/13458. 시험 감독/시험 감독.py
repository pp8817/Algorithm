import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
arr = list(map(int, input().split()))
B,C = map(int, input().split())

ans = 0

for a in arr:
    a -= B
    ans += 1
    if a>0:
        if a%C==0:
            ans += (a//C)
        else:
            ans += (a//C+1)
print(ans)