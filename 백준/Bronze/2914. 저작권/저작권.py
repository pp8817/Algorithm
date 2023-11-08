import sys
input = lambda: sys.stdin.readline().rstrip()

A, I = map(int, input().split())

print(A * (I-1) +1)