def solution(park, routes):
    W = len(park)
    H = len(park[0])
    
    x, y = 0,0
    
    for i in range(W):
        for j in range(H):
            if park[i][j] == "S":
                x, y = i,j
                break
    
    dic = {"N": [-1,0], "S":[1,0], "W":[0,-1], "E": [0,1]}
    
    for i in range(len(routes)):
        d, s = routes[i][0], int(routes[i][2])
        [dx, dy] = dic[d]
        nx, ny = x+dx*s, y+dy*s
        
        if 0<=nx<W and 0<=ny<H:
            if promising(x, y, nx, ny, park):
                x, y = nx, ny
    return [x, y]

def promising(x, y, nx, ny, park):
    if x == nx:  # 이동 방향이 수평일 때
        start, end = min(y, ny), max(y, ny)
        for c in range(start, end + 1):
            if park[x][c] == "X":
                return False
    else:  # 이동 방향이 수직일 때
        start, end = min(x, nx), max(x, nx)
        for r in range(start, end + 1):
            if park[r][y] == "X":
                return False
    return True