import itertools
import math

def solution(numbers):
    answer = 0
    arr = [i for i in numbers]
    arr2 = set()
    
    for i in range(1, len(arr)+1):
        nPr = list(itertools.permutations(arr, i))
        for j in nPr:
            n = ""
            for k in j:
                n += k
            n = int(n)
            arr2.add(n)
            
    for n in arr2:
        if check(n):
            answer += 1
    
    return answer

def check(n):
    if n<=1:
        return False
    for i in range(2, int(math.sqrt(n)+1)):
        if n % i == 0:
            return False
    return True
    


