def solution(answers):
    answer = []
    pattern1 = [1,2,3,4,5]*2000
    pattern2 = [2, 1, 2, 3, 2, 4, 2, 5]*1250
    pattern3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]*1000
    
    res = [0,0,0]
    for i, ans in enumerate(answers):
        if pattern1[i] == ans:
            res[0] += 1
        if pattern2[i] == ans:
            res[1] += 1
        if pattern3[i] == ans:
            res[2] += 1
    
    ans = []
    m = max(res)
    for i, c in enumerate(res):
        if res[i] == m:
            ans.append(i+1)
    
    return ans
    