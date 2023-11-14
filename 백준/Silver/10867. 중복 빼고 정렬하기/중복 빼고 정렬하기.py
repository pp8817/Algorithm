import sys
input = lambda: sys.stdin.readline().rstrip()
N = int(input())
s = set(map(int, input().split()))
li = list(s)
li.sort()
print(*li)