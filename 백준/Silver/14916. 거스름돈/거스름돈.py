import sys
input = sys.stdin.readline

n = int(input())
answer = 0

i = 0
f = 0
while True:
    if (n%5)==0:
        answer += (i+(n//5))
        n=0
        break
    n -= 2 
    i += 1
    if n < 0:
        break
if n<0:
    print(-1)
else:
    print(answer)