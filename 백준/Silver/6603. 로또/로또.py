import sys
input = lambda: sys.stdin.readline().rstrip()

def dfs(start):
    if len(s) == 6:
        print(*s) 
        return
    
    for i in range(start, k):
        s.append(S[i])
        dfs(i+1)
        s.pop()

while True:
    global k, S
    S = list(map(int, input().split()))
    k, S = S[0], S[1:]
    if k == 0:
        break

    s = []
    dfs(0)
    print()