import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())

cnt = 1
s = 6
count = 1

while n > cnt:
    cnt += s
    s += 6
    count +=1
print(count)