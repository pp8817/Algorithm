import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
A = list(map(int, input().split()))

# 0~(양수가 되는 지점 전)까지의 각 점을 팀원 중 한 명으로 삼고 투 포인터 방식으로 전개
A.sort()

S = N-2
for i in range(N):
    if A[i] > 0:
        S = i
        break

dict = {}
for a in A:
    if a in dict:
        dict[a] += 1
    else:
        dict[a] = 1

ans = 0
for i in range(0,S):
    tmp = A[i]
    start,end = i+1, N-1
    while start < end:
        s = tmp + A[start] + A[end]

        if s==0:
            if A[start] == A[end]:
                ans += end - start
            else:
                ans += dict[A[end]]
            start += 1

        elif s < 0: # s가 0보다 작다면 값을 키워야함
            start += 1
        else: # s가 0보다 크다면 값을 작게 해야됨
            end -= 1

print(ans)