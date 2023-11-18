import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
li = []
for _ in range(N):
    li.append(int(input()))
li = sorted(li)

W = 0
i = 0
while len(li) != 0:
    i+=1
    w = li.pop()
    if W < w * i:
        W = w * i
print(W) 