import sys
input = lambda: sys.stdin.readline().rstrip()

def change(num):
    if switch[num] == 0:
        switch[num] = 1
    else:
        switch[num] = 0
    return

N = int(input())
switch = [0] + list(map(int, input().split()))
T = int(input())
for _ in range(T):
    s, num = map(int, input().split())

    if s == 1: # 남자인 경우
        for i in range(num, N+1, num):
            change(i)
    else: # 여자인 경우
        change(num)
        for i in range(N//2):
            if (num+i)>N or (num-i)<1: break
            if switch[num-i] == switch[num+i]:
                change(num-i)
                change(num+i)
            else:
                break
        
for i in range(1, N+1):
    print(switch[i], end = " ")
    if i%20 == 0:
        print()