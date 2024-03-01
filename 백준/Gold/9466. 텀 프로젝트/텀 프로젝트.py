import sys
sys.setrecursionlimit(10**6)

T = int(input())
for _ in range(T):
    N = int(input())
    selected = [0] + list(map(int, input().split()))

    visited = [False] * (N+1)
    team_mems = 0

    def dfs(i):
        global team_mems

        visited[i] = True # 나부터
        team.append(i) # 팀 후보에 추가
        select = selected[i] # 다음 사람 지목

        if visited[select]: # 지목한 사람을 이미 방문했을 경우
            if select in team: # 그 사람이 팀 후보에 있다면
            	# 그 사람부터 이후에 팀에 들어온 사람들은 한 팀이 된다
                team_mems += len(team[team.index(select):])
        else: # 아니라면 지목 받은 사람이 다른 사람 지목
            dfs(select)

    for i in range(1, N+1):
        if not visited[i]:
            team = []
            dfs(i)

    print(N - team_mems)