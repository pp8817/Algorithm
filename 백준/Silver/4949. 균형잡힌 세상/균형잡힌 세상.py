import sys
input = lambda: sys.stdin.readline().rstrip()
def check(s):
    stack = []
    for i in s:
        if i in "([":
            stack.append(i)
        elif i in ")]":
            if len(stack) == 0:
                return "no"
            elif dic[i] == stack[-1]:
                stack.pop()
            else:
                return "no"
    if len(stack) == 0:
        return "yes"
    else:
        return "no"
    
dic = {")":"(","]":'['} 
   
while True:
    s = input()
    if s == '.':
        break
    else:
        print(check(s))