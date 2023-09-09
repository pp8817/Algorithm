n, m = map(int, input().split())

li = list(range(1, n+1))
for _ in range(m):
    a, b = map(int, input().split())
    ex = li[a-1:b]
    for i in range(a-1, b):
        li[i] = ex[(b-1)-i]
print(' '.join(map(str, li)))