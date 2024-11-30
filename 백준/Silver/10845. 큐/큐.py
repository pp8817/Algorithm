import sys
n=int(sys.stdin.readline())
q=[]
for _ in range(n):
    order=sys.stdin.readline().split()
    if order[0]=='push':
        q.append(order[1])
    if order[0]=='pop':
        if len(q)>0:
            print(q[0])
            q.pop(0)
        else:
            print(-1)
    if order[0]=='size':
        print(len(q))
    if order[0]=='empty':
        if len(q)==0:
            print(1)
        else:
            print(0)
    if order[0]=='front':
        if len(q)==0:
            print(-1)
        else:
            print(q[0])
    if order[0]=='back':
        if len(q)==0:
            print(-1)
        else:
            print(q[-1])