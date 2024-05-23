import sys
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())

# # 1부터 N까지의 자연수 중에서 M개를 고른 수열
# # 같은 수 중복 가능
# # 고른 수열은 비내림차순이어야 한다 -> 오름차순

n = []
def dfs():
    if len(n) == M:
        print(" ".join(map(str, n)))
        return 
    for i in range(1, N+1):
        if promising(i):
            dfs()
            n.pop()

def promising(i):
    n.append(i)
    a = 0
    for i in n:
        if a<=i:
            a = i
        else:
            n.pop()
            return False
    return True

dfs()