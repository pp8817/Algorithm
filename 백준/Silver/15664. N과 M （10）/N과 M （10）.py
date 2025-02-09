import sys
input = lambda: sys.stdin.readline().rstrip()

# 길이가 M인 수열, 비내림차순(오름차순)
def dfs(ans, idx):
    if len(ans) == M:
        print(*ans)
        return
    
    temp = 0
    for i in range(idx, N):
        if not checked[i] and temp != arr[i]:
            temp = arr[i]
            ans.append(arr[i])
            checked[i] = True

            dfs(ans, i+1)

            ans.pop()
            checked[i] = False

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

checked = [False]*N
ans = []
dfs(ans, 0)