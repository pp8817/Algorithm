import sys
input = lambda: sys.stdin.readline().rstrip()

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    
    n = 1
    m = 1
    for _ in range(N):
        m*=M
        M-=1
        
    for i in range(2, N+1):
        n*=i
    print(int(m/n))