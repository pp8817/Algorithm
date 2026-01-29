import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())

last = [-1]*11
ans = 0
for _ in range(N):
    cow, pos = map(int, input().split())
    if last[cow] == -1:
        last[cow] = pos
    elif last[cow] != pos: 
        ans += 1
        last[cow] = pos
print(ans)