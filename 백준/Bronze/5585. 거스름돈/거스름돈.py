import sys
input = sys.stdin.readline

p = 1000 - int(input())

count = 0
for i in [500, 100, 50, 10, 5, 1]:
    count += p//i
    p = p%i

print(count)