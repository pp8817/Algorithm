import sys
input = lambda: sys.stdin.readline().rstrip()

def solve():
    N, K = map(int, input().split())
    courses = list(map(int, input().split()))

    # 가는 과정
    for i in range(N):
        if K < courses[i]:
            print(i+1)
            return
        K -= courses[i]
    
    for i in range(N-1, -1, -1):
        if K < courses[i]:
            print(i+1)
            return
        K -= courses[i]

solve()