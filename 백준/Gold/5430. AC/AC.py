import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

def sol(p, arr):
    rev = 0
    for s in p:
        if s == 'R':
            rev += 1
        elif s == 'D':
            if len(arr) == 0:
                return "error"
            else:
                if rev % 2==0:
                    arr.popleft()
                else:
                    arr.pop()
    if rev%2 != 0:
        arr.reverse()
    result = "["
    if len(arr)!=0:
        for i in range(len(arr)-1):
            result += str(arr[i])
            result += ","
        result += str(arr[-1])
    result += "]"
    return result
    


T = int(input())

for i in range(T):
    p = input()
    n = int(input())
    if n>0:
        arr = input()[1:-1]
        arr = deque(map(int, arr.split(',')))
        print(sol(p, arr))
    else:
        arr = input()
        if "D" in p:
            print('error')
        else:
            print("[]")