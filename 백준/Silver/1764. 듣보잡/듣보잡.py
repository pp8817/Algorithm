import sys
input = lambda: sys.stdin.readline().rstrip()
n, m = map(int, input().split())
arr = set()
li = []
for _ in range(n):
    arr.add(input())
for _ in range(m):
    no = input()
    if no in arr:
        li.append(no)
print(len(li))
li = sorted(li)
for j in li:
    print(j)