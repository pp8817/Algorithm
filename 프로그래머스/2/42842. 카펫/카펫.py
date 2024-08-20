def solution(brown, yellow):
    a,b = 0,0
    
    for i in range(1, 99999999):
        if yellow%i == 0:
            a = yellow//i
            b = i
            
            if 2*(a+b+2) == brown:
                break
    
    return [a+2,b+2]