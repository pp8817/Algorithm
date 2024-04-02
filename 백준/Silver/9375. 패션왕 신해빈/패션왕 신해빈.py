import sys
input = lambda: sys.stdin.readline().rstrip()

T = int(input())
for _ in range(T):
    n = int(input())
    dic = {}
    for _ in range(n):
        name, category = input().split()
        if category in dic:
            dic[category].append(name)
        else: 
            dic[category] = [name]

    cnt = 1
    for i in dic:
        cnt *= (len(dic[i])+1)
    print(cnt-1)