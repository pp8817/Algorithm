import sys
input = lambda: sys.stdin.readline().rstrip()

X = int(input())

line = 1
#라인 찾기
while X>line:
    X -= line
    line+=1
if line % 2==0:
    mo = line-X+1
    za = X
else:
    mo = X
    za = line-X+1
print(f"{za}/{mo}")