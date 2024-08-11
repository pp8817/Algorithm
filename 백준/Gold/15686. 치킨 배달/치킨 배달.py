import sys
input = lambda: sys.stdin.readline().rstrip()

def dfs(idx, cnt):

    global min_ans

    if cnt == M:
        
        ans = 0

        for i in home:
            distance = float("inf")
            for j in range(len(visited)):
                if visited[j]:
                    check_num = abs(i[0]-chicken[j][0])+abs(i[1]-chicken[j][1])
                    distance = min(distance, check_num)

            ans += distance
        min_ans = min(ans, min_ans)

        return
    
    for i in range(idx, len(chicken)):
        if not visited[i]:

            visited[i] = True
            dfs(i+1, cnt+1)
            visited[i] = False


N, M = map(int, input().split())

min_ans = float("inf")

home = []
chicken = []

for i in range(N):
    row = list(map(int, input().split()))

    for j in range(N):
        if row[j] == 1:
            home.append((i,j))
        elif row[j] == 2:
            chicken.append((i,j))

visited = [False]*len(chicken)

dfs(0,0)
print(min_ans)