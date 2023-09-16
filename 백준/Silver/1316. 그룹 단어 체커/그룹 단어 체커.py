n=int(input())
answer=0
for _ in range(n):
    w=input()
    error=0
    for i in range(len(w)-1):
        if w[i] != w[i+1]:
            nw=w[i+1:]
            if nw.count(w[i])>0:
                error+=1
    if error==0:
        answer+=1
print(answer)