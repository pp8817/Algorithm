def solution(numbers, hand):
    answer = []
    left_num = [1,4,7]
    right_num = [3,6,9]
    middle_num = [2,5,8,9]
    
    if hand == "left":
        hand = "L"
    else:
        hand = "R"
    
    pos = {
    1: (0,0), 2: (0,1), 3: (0,2),
    4: (1,0), 5: (1,1), 6: (1,2),
    7: (2,0), 8: (2,1), 9: (2,2),
    '*': (3,0), 0: (3,1), '#': (3,2)
    }
    
    left, right = pos["*"], pos["#"]
    
    for num in numbers:
        if num in left_num:
            answer.append("L")
            left = pos[num]
        elif num in right_num:
            answer.append("R")
            right = pos[num]
        else:
            x, y = pos[num]
            l_dist = abs(left[0] - pos[num][0]) + abs(left[1] - pos[num][1])
            r_dist = abs(right[0] - pos[num][0]) + abs(right[1] - pos[num][1])
            
            if l_dist < r_dist:
                answer.append("L")  
                left = pos[num]
            elif r_dist < l_dist:
                answer.append("R")
                right = pos[num]
            else:
                answer.append(hand)
                if hand == "L":
                    left = pos[num]
                else:
                    right = pos[num]
    
    return "".join(answer)