def solution(dirs):
    answer = 0
    
    move = {'U': (0, 1), 'D': (0, -1), 'R': (1, 0), 'L': (-1, 0)}
    x, y = 0, 0
    edges = set()
    
    for com in dirs:
        dx, dy = move[com]
        nx, ny = x + dx, y + dy
        
        if -5<=nx<=5 and -5<=ny<=5:
            if (x,y) < (nx, ny):
                edge = (x, y, nx, ny)
            else:
                edge = (nx, ny, x, y)
            edges.add(edge)
            x,y = nx, ny
            
    return len(edges)