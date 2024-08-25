from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    graph = [[-1]*102 for _ in range(102)]
    visited = [[1]*102 for _ in range(102)]
    
    # graph 정리
    for rec in rectangle:
        x1,y1,x2,y2 = map(lambda x: 2*x, rec)
        
        for x in range(x1, x2+1):
            for y in range(y1,y2+1):
                # 테두리를 제외한 점은 사각형 내부이기 때문에 0
                if x1<x<x2 and y1<y<y2:
                    graph[x][y] = 0
                # 테두리의 점이 다른 사격형의 내부가 아니라면 1
                elif graph[x][y] != 0:
                    graph[x][y] = 1
    
    
    item = (itemX*2, itemY*2)
    start = (characterX*2, characterY*2)
    q = deque()
    q.append(start)
    
    while q:
        current_x, current_y = q.popleft()
        
        if (current_x, current_y) == item:
            return visited[current_x][current_y]//2
        
        for (rx, ry) in ((1,0), (0,1), (-1,0), (0,-1)):
            nx, ny = current_x+rx, current_y+ry
            if graph[nx][ny] == 1 and visited[nx][ny] == 1:
                visited[nx][ny] = visited[current_x][current_y]+1
                q.append((nx,ny))
                