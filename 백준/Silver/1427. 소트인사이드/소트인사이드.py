n=str(input())
t=[]
for i in n:
    t.append(int(i))
t.sort(reverse=True)
for j in t:
    print(j,end='')