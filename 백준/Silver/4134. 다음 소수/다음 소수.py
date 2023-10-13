import sys
input = lambda: sys.stdin.readline().rstrip()
import math
n = int(input())
for _ in range(n):
    s = int(input())
    s = s-1
    while 1:
        s += 1
        if s in [0,1,2]:
            print(2)
            break
                
        if s % 2!=0:
            c = 0
            if s in [0,1,2]:
                print(s)
            for i in range(3, int(math.sqrt(s))+1):
                if s%i == 0:
                    c += 1
                    break
            if c == 0:
                print(s)
                break
            else:
                s += 1
                continue