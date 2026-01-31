import sys
input = lambda: sys.stdin.readline().rstrip()

N, Q = map(int, input().split())
A = list(map(int, input().split()))
Q_arr = list(map(int, input().split()))
teams = [0] * N

# 누적합으로 풀면 될 듯?
# 먼저 각 소가 끝 점인? 경우의 합을 구해두고, 순회하면서 체크
for i in range(N):
    val = 1
    for j in range(4):
        val *= A[(i + j) % N]
    teams[i] = val

total_S = sum(teams)

for idx in Q_arr:
    target = idx - 1
    for j in range(4):
        team_idx = (target-j) % N
        total_S -= teams[team_idx]
        teams[team_idx] *= -1
        total_S += teams[team_idx]

    A[target] *= -1
    print(total_S)