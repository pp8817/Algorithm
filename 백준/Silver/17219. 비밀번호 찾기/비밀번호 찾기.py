import sys
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())

dic = {}
for _ in range(N):
    di, password = input().split()
    dic[di] = password
for _ in range(M):
    print(dic[input()])