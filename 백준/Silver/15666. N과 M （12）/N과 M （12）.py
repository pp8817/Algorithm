import sys
input = lambda: sys.stdin.readline().rstrip()

def back(s):
    if len(ans) == M:
        print(*ans)
        return
    a=0
    for i in range(s, N):
        if nums[i] != a:
            ans.append(nums[i])
            a = nums[i]
            back(i)
            ans.pop()


# 같은 수 중복 가능, 오름차순, 중복되는 수열 출력 X, 사전 순으로 증가하도록
N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

ans = []
check=[]
visited = [False]*(N+1)
back(0)