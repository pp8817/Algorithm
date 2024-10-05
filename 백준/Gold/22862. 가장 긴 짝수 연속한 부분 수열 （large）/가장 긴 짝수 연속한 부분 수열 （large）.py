import sys
input = lambda: sys.stdin.readline().rstrip()

N, K = map(int, input().split())
arr = list(map(int, input().split()))

start, end = 0,0
ans = 0
cnt = 0 # 홀수의 갯수

while end < N:
    if cnt > K: # 홀수의 갯수가 K보다 클 때
        if arr[start]%2: # 시작점의 값이 홀수라면
            cnt -= 1 # 홀수 갯수 -1

        start += 1
    else: # 홀수의 갯수가 K보다 작을 때
        if arr[end]%2: # 도달한 점의 값이 홀수라면
            cnt += 1 # 홀수 갯수 +1
        end += 1

    if cnt <= K: # 홀수의 갯수가 K보다 작다면
        ans = max(ans, end-start-cnt)
print(ans)