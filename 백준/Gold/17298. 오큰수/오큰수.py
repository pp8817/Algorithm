import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
arr = list(map(int, input().split()))

# Ai의 오큰수: 오른쪽에 있으면서 Ai보다 큰 수 중에서 가장 왼쪽에 있는 수
ans = [-1]*N
stack = []

for i in range(N):
    while stack:
        if stack[-1][1] < arr[i]:
            ans[stack[-1][0]] = arr[i]
            stack.pop()
        else: # stack[-1][1] > arr[i]
            break

    stack.append((i, arr[i]))

print(*ans)