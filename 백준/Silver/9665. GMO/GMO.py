import sys
input = lambda: sys.stdin.readline().rstrip()

apple = input()
pig = input()
insert_cost = list(map(int, input().split()))  # A, C, G, T

cost_map = {'A': insert_cost[0], 'C': insert_cost[1], 'G': insert_cost[2], 'T': insert_cost[3]}

N, M = len(apple), len(pig)
ans = float('inf')

# 사과 DNA의 0~N 사이의 모든 위치에 삽입 시도
for i in range(N + 1):
    total_cost = 0
    a_idx = i
    for j in range(M):
        if a_idx < N and apple[a_idx] == pig[j]:
            # 문자가 같으면 삽입 필요 없음
            a_idx += 1
        else:
            # 삽입해야 함
            total_cost += cost_map[pig[j]]
    ans = min(ans, total_cost)

print(ans)