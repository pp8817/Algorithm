import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
A = list(map(int, input().split()))
reverse_A = A[::-1]

increase = [1]*N # 가장 긴 증가하는 부분 수열
decrease = [1]*N # 가장 긴 감소하는 부분 수열

for i in range(N):
    for j in range(i):
        if A[i] > A[j]:
            increase[i] = max(increase[i], increase[j]+1)
        if reverse_A[i] > reverse_A[j]:
            decrease[i] = max(decrease[i], decrease[j]+1)

result = [0]*N
for i in range(N):
    result[i] = increase[i] + decrease[N-i-1] - 1

print(max(result))