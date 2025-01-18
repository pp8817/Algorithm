import sys
input = lambda: sys.stdin.readline().rstrip()

# 팰린드롬: 원본과 reverse가 동일한 수열, 문자열
N = int(input())
arr = list(input().split())

dp = [[0]*N for _ in range(N)] # dp[i][j]: i~j번째 숫자의 팰린드롬 여ㅜ부

for i in range(N):
    dp[i][i] = 1

for i in range(N-1):
    if arr[i] == arr[i+1]:
        dp[i][i+1] = 1

for i in range(N-2):
    for j in range(N-2-i):
        k = i+j+2
        if arr[j] == arr[k] and dp[j+1][k-1]:
            dp[j][k] = 1

M = int(input()) # 질문 개수
for _ in range(M):
    S,E = map(int, input().split()) # arr의 S번째 수부터 E번째 까지 
    print(dp[S-1][E-1])