import sys
input = lambda: sys.stdin.readline().rstrip()

# 면적 구하기

N = int(input()) # 3<=N<=10,000

xy = []
for _ in range(N):
    xy.append(list(map(int, input().split())))

xy.append(xy[0])

a,b = 0,0
for i  in range(N):
    a += xy[i][0]*xy[i+1][1]
    b += xy[i][1]*xy[i+1][0]

print(abs(a-b)/2)