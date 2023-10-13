k=int(input())
t=[0]
for _ in range(k):
    a=int(input())
    if a==0:
        del t[len(t)-1]
    else:
        t.append(a)
print(sum(t))