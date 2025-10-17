import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

N, W, L = map(int, input().split())
truck_weights = deque(map(int, input().split()))

bridge = deque([0]*W)
time = 0
truck_index = 0
total_weight = 0

while truck_index < N:
    time += 1

    # 트럭 한 칸 이동
    left_truck = bridge.popleft()
    total_weight -= left_truck

    # 다음 트럭이 올라갈 수 있다면
    if total_weight + truck_weights[truck_index] <= L:
        bridge.append(truck_weights[truck_index])
        total_weight += truck_weights[truck_index]
        truck_index += 1
    else:
        bridge.append(0)

print(time+W)