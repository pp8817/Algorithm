from collections import deque

def solution(bridge_length, weight, truck_weights):
    
    time = 0
    bridge = deque([0] * bridge_length)
    truck_weights = deque(truck_weights)
    
    currentWeight = 0
    while truck_weights:
        time += 1

        currentWeight -= bridge.popleft()

        if currentWeight + truck_weights[0] <= weight:
            x = truck_weights.popleft()
            currentWeight += x
            bridge.append(x)

        else: 
            bridge.append(0)
            
    time += bridge_length
    
    return time