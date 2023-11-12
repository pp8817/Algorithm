import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
A = sorted(map(int, input().split()))
B = sorted(map(int, input().split()), reverse=True)
s = 0
for a, b in zip(A, B):
    s+=a*b
print(s)