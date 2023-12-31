n,k=map(int, input().split())
li=list(i for i in range(1,n+1))
answer=[]
num=0
for i in range(n):
    num+=k-1
    if num>=len(li):
        num=num%len(li)
    answer.append(str(li.pop(num)))
print("<",", ".join(answer)[:],">", sep='')  