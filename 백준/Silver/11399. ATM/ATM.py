import sys
input = sys.stdin.readline

N = int(input()) #N^2
P = map(int, input().split())

P = sorted(P, reverse=True)
total=0

for i, p in enumerate(P):
    total += (i+1)*p
    
print(total)