import sys
input = sys.stdin.readline

N = int(input())
ml = list(map(int, input().split()))

ml = sorted(ml)
total = 0
for i in range(N-1):
    total += ml[i]*0.5
print(total + ml[-1])