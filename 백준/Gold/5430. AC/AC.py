import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

def sol(p, arr):
    flag = 0 # 0: popleft, 1: pop
    for cmd in p:
        if cmd == "R": # 뒤집기
            if flag:
                flag = 0
            else:
                flag = 1
        elif cmd == "D":
            if len(arr) == 0:
                return "error"

            if flag: # flag == 1
                arr.pop()
            else:
                arr.popleft()

    result = "["
    if len(arr) != 0:
        if flag:
            arr.reverse()
        
        for i in range(len(arr)-1):
            result += str(arr[i])
            result += ','
        result += str(arr[-1])
    result += "]"
    return result
    
T = int(input())

for i in range(T):
    p = input()
    n = int(input())
    if n>0:
        arr = deque(map(int, input()[1:-1].split(',')))
        print(sol(p, arr))
    else:
        arr = input()
        if "D" in p:
            print('error')
        else:
            print("[]")