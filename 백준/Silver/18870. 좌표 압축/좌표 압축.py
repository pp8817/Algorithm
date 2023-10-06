import sys
n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

res = sorted(list(set(arr)))

dic = {res[i] : i for i in range(len(res))}
for i in arr:
    print(dic[i], end=' ')