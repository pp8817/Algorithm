def solution(n,a,b):
    
    ans = 0
    while a != b:
        ans += 1
        a, b = (a+1)//2, (b+1)//2
    
    return ans