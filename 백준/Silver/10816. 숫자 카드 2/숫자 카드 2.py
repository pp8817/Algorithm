import sys
input = sys.stdin.readline
n = int(input())
card = list(map(int, input().split()))
s = set(list(card))
dic = {}
for  i in s:
    dic[i] = 0
for i in card:
    dic[i] +=1

m = int(input())
check = list(map(int, input().split()))
for j in check:
    if j in dic:
        print(dic[j], end=' ')
    else:
        print(0, end=' ')