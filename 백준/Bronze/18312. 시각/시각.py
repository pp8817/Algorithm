import sys
input = lambda: sys.stdin.readline().rstrip()

N, K = map(int, input().split())
K = str(K)

ans = 0
for i in range(N+1): # 0~59
    if i < 10:
        i = '0' + str(i)
    for j in range(60): # 0~59
        if j < 10:
            j = '0' + str(j)
        for k in range(60):
            if k < 10:
                k = '0' + str(k)
            if K in (str(i)+str(j)+str(k)):
                ans += 1

print(ans)