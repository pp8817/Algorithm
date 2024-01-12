import sys
from collections import deque
 
n,m = map(int,sys.stdin.readline().split())
array=[[] for _ in range(n)]
 
#띄어쓰기 없는 아이들 입력 받기
for i in range(n):
    str = sys.stdin.readline().strip()
    for j in range(m):
        array[i].append(int(str[j]))
 
#d가 갈 수 있는 범위
d = [[1,0],[0,1],[-1,0],[0,-1]]
#bfs
def bfs(y,x):
    queue = deque()
    queue.append((y,x))
    while queue:
        y1,x1 = queue.popleft()
        for dx,dy in d:
            if 0<=y1+dy<n and 0<=x1+dx<m:
                if array[y1+dy][x1+dx]==1:
                    array[y1+dy][x1+dx]=array[y1][x1]+1
                    queue.append((y1+dy,x1+dx))
 
 
#(1,1)에서 처음 시작하므로
bfs(0,0)
print(array[n-1][m-1])