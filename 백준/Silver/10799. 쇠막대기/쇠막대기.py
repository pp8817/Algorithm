import sys
s=list(sys.stdin.readline())
answer=0
stack=[]
for i in range(len(s)):
    if s[i]=='(':
        stack.append(s[i])

    elif s[i]==')':
        if s[i-1]=='(':
            stack.pop()
            answer+=len(stack)
        else:
            answer+=1
            stack.pop()
print(answer)