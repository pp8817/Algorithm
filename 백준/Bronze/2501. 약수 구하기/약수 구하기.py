n, k=map(int, input().split())
a=[]
for i in range(1,n+1):
    if n%i==0:
        a.append(i)
a.sort()
if len(a) >= k:
    print(a[k-1])
else:
    print(0)
