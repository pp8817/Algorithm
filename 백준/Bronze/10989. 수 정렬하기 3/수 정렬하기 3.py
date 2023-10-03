import sys
input = sys.stdin.readline
li = [0] * 10001

for _ in range(int(input())):
    li[int(input())] += 1

for i in range(10001):
    for _ in range(li[i]):
        print(i)