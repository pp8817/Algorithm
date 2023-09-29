n=int(input())
arr=0
for i in range(1,n+1):
    a=list(map(int, str(i)))
    arr=i+sum(a)
    if arr==n:
        print(i)
        break
    elif i==n:
        print(0)