import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
arr = list(map(int, input().split()))
operators = list(map(int, input().split()))

mx, mn = int(-1e9), int(1e9)

def dfs(n, temp): # index, value
    global mx, mn

    if n == (N-1):
        mx = max(mx, temp)
        mn = min(mn, temp)
        return
    
    if operators[0] != 0:
        operators[0] -= 1
        dfs(n+1, temp+arr[n+1])
        operators[0] += 1

    if operators[1] != 0:
        operators[1] -= 1
        dfs(n+1, temp-arr[n+1])
        operators[1] += 1

    if operators[2] != 0:
        operators[2] -= 1
        dfs(n+1, temp*arr[n+1])
        operators[2] += 1

    if operators[3] != 0:
        operators[3] -= 1
        dfs(n+1, int(temp/arr[n+1]))
        operators[3] += 1

dfs(0,arr[0])
print(mx)
print(mn)