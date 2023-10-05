import sys
n=int(sys.stdin.readline())
t=[]
for _ in range(n):
    a,b=sys.stdin.readline().split()
    a=int(a)
    t.append((a,b))
#나이를 기준으로 정렬
t.sort(key=lambda x:x[0])
for i in t:
    print(i[0],i[1])