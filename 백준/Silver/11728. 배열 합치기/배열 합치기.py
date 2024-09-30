import sys
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = sorted((A+B))
print(*C)