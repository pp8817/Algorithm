import sys
input = lambda: sys.stdin.readline()

# 크기가 M인 수열, 같은 수 중복 가능
# 중복 수열 x, 사전 순 오름차순
def dfs(num):
    if len(num) == M:
        print(*num)
        return
    for a in arr:
        num.append(a)
        dfs(num)
        num.pop()

N, M = map(int, input().split())
# set을 이용해 중복을 제거 -> list로 변환 후 오름차순 정렬
arr = list(set(list(map(int, input().split()))))
arr.sort()

num = []

dfs(num)