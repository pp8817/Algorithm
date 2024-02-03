import sys
input = sys.stdin.readline
from collections import deque
import copy
from itertools import combinations

n, m = map(int, input().split())
graph=[]
d = [[0, 1], [0,-1], [1,0], [-1,0]]

for _ in range(n):
    graph.append(list(map(int, input().split())))
    
def bfs(tmp_graph):
    queue = deque()
    
    for i in range(n):
        for j in range(m):
            if tmp_graph[i][j] == 2:
                queue.append((i, j))
    while queue:
        x, y = queue.popleft()
        
        for dx, dy in d:
            nx, ny = x+dx, y+dy
            
            if 0<=nx<n and 0<=ny<m and tmp_graph[nx][ny] == 0:
                tmp_graph[nx][ny] = 2
                queue.append((nx, ny))
    global answer
    cnt = 0
    
    for i in range(n):
        cnt += tmp_graph[i].count(0)            
    answer = max(answer, cnt)  
                
answer = 0

xy = [(x,y) for x in range(n) for y in range(m) if not graph[x][y]]

for c in combinations(xy, 3): # 시간 복잡도를 고려하여 조합을 사용해서 벽을 세울 위치를 정함
    tmp_graph = copy.deepcopy(graph)
    for x, y in c:
        tmp_graph[x][y] = 1
    bfs(tmp_graph)

print(answer)