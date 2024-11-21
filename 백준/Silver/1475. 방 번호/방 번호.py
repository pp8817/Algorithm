import sys
input = lambda: sys.stdin.readline().rstrip()

ans = 0
N = input()
dic = {i:0 for i in range(10)}

for i in N:
    num = int(i)
    if num == 6:
        dic[9] += 1
    else:
        dic[num] += 1

if dic[9]%2:
    dic[9] = (dic[9]//2)+1
else:
    dic[9] //= 2

print(max(dic.values()))