import sys
input = lambda: sys.stdin.readline().rstrip()

T = int(input())

for _ in range(T):
    s = list(input())
    N = len(s)

    pivot = -1
    for i in range(N-1, 0, -1):
        if s[i-1] < s[i]:
            pivot = i-1
            break
    
    if pivot == -1:
        print("".join(s))
        continue
    
    for j in range(N - 1, pivot, -1):
        if s[j] > s[pivot]:
            s[pivot], s[j] = s[j], s[pivot]
            break
    
    s[pivot+1:] = reversed(s[pivot+1:])
    
    print("".join(s))