import sys
input = sys.stdin.readline
n = int(input())
card = list(map(int, input().split()))
m = int(input())
check = list(map(int, input().split()))
dic = {}
for i in card:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1
for j in check:
    if j in dic:
        print(dic[j], end=' ')
    else:
        print(0, end=' ')