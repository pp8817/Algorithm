import sys
input = lambda: sys.stdin.readline().rstrip()

T = int(input())

for _ in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    print(min(arr), max(arr))