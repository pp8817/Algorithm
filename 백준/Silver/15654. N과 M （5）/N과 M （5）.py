import sys
input = lambda: sys.stdin.readline().rstrip()

def back():
    if len(ans) == M:
        print(" ".join(map(str, ans)))
        return
    for i in range(len(m)):
        if m[i] not in ans:
            ans.append(m[i])
            back()
            ans.pop()

N, M = map(int, input().split())

m = sorted(list(map(int, input().split())))

ans = []
back()