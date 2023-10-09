import sys
input = sys.stdin.readline
n, m = map(int, input().split())

dic = {}
for i in range(1, n+1):
    name = input().rstrip()
    dic[i] = name
    dic[name] = i

for j in range(m):
    pok = input().rstrip()
    if pok.isdigit():
        print(dic[int(pok)])
    else:
        print(dic[pok])