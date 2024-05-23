import sys
input = lambda: sys.stdin.readline().rstrip()

def back(s):
    if len(ans) == M:
        print(" ".join(map(str, ans)))
        return
    for i in range(s, len(m)):
        ans.append(m[i])
        back(i)
        ans.pop()

N, M = map(int, input().split())

m = sorted(list(map(int, input().split())))

ans = []
back(0)