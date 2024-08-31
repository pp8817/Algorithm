def solution(answers):
    answer = []
    a = [1,2,3,4,5]*2000
    b = [2,1,2,3,2,4,2,5]*1250
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]*1000
    count = [0,0,0]
    for i, ans in enumerate(answers):
        if a[i] == ans:
            count[0] += 1
        if b[i] == ans:
            count[1] += 1
        if c[i] == ans:
            count[2] += 1
    
    m = 0
    for i, value in enumerate(count):
        if value == max(count):
            answer.append(i+1)
    return answer