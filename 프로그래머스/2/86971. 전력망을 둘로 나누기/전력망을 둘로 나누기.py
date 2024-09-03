from collections import deque

def bfs(graph, n):
    visited = [1]*n
    num1, num2 = 1, 0
    
    q = deque()
    q.append(0)
    visited[0] = 0
    
    while q:
        v = q.popleft()
        
        for i in graph[v]:
            if visited[i]:
                visited[i] = 0
                q.append(i)
                num1 += 1
            
    num2 = sum(visited)
    return num1, num2 

def solution(n, wires):
    answer = n
    for i in range(n-1):
        graph = [[] for _ in range(n)]
        arr = wires[:i] + wires[i+1:]
        
        for s,t in arr:
            graph[s-1].append(t-1)
            graph[t-1].append(s-1)
        num1, num2 = bfs(graph, n)
        answer = min(answer, abs(num1-num2))

    return answer