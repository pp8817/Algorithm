import sys
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())

print(abs(N-M))