import sys
input = lambda: sys.stdin.readline().rstrip()

infix = list(input())
stack = [] # 피연산자가 들어갈 리스트
postfix = "" # 후위표기식으로 변환한 결과

for s in infix:
    if s.isalpha():
        postfix += s
    else:
        if s == "(":
            stack.append(s)
        elif s in ["*", "/"]: # 새로운 최우선 피연산자가 나왔어 -> 스택에 피연산자가 존재하고 이전 피연산자가 "*" or "/"라면 그거는 후위 표기식에 붙이고
            while stack and (stack[-1] in ["*","/"]):
                postfix += stack.pop()
            stack.append(s)
        elif s in ["+", "-"]: # 스택에 피연산자가 존재하고, 괄호 연산이 아니라면
            while stack and stack[-1] != "(":
                postfix += stack.pop()
            stack.append(s)
        elif s == ")":
            while stack and stack[-1] != "(":
                postfix += stack.pop()
            stack.pop()
while stack:
    postfix += stack.pop()
print(postfix)
