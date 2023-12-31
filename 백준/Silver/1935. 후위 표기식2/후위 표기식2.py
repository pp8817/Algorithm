import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

N = int(input())
Pe = input()
li = [0]*N

for i in range(N):
    li[i] = int(input())

stack = []

for i in Pe:
    if "A" <= i <= "Z":
        stack.append(li[ord(i)-ord('A')])
    else:
        s2 = stack.pop() 
        s1 = stack.pop() 
        
        if i == "+":
            stack.append(s1+s2)
        elif i == '-' :
            stack.append(s1-s2)
        elif i == '*' :
            stack.append(s1*s2)
        else:
            stack.append(s1/s2)
print("%.2f"%stack[0])