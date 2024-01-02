n=int(input())
arr=1
stack=[]
answer=[]
flag=0
for i in range(n):
    num=int(input())
    while arr<=num: #입력한 수가 나올 때까지 push
        stack.append(arr)
        answer.append('+') #push될 때마다 +출력
        arr+=1 #arr의 값을 1씩 더해주면서 탐색
    if stack[-1]==num: 
        stack.pop()
        answer.append('-')
    else:
        print('NO')
        flag+=1
        break
if flag==0:
    for j in answer:
        print(j)