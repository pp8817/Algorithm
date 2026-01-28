def solution(numbers, hand):
    maps = {1: [0,0], 2: [0,1], 3: [0,2],
           4: [1,0],5: [1,1],6: [1,2],
           7: [2,0],8: [2,1],9: [2,2],
           0: [3,1],}
            
    left_start = (3,0)
    right_start = (3,2)
    
    answer = ""
    
    for num in numbers:
        if num in [1,4,7]:
            answer += "L"
            left_start = maps[num]
        
        elif num in [3,6,9]:
            answer += "R"
            right_start = maps[num]
        else:
            point = maps[num]
            left_distance = abs(point[0] - left_start[0]) + abs(point[1] - left_start[1])
            right_distance = abs(point[0] - right_start[0]) + abs(point[1] - right_start[1])
            
            if left_distance > right_distance:
                answer += "R"
                right_start = maps[num]
            elif left_distance < right_distance:
                answer += "L"
                left_start = maps[num]
            else:
                if hand == "left":
                    answer += "L"
                    left_start = maps[num]
                else:
                    answer += "R"
                    right_start = maps[num]
    return answer
                
            
            