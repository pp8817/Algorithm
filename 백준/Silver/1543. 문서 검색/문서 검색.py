import sys
input = lambda: sys.stdin.readline().rstrip()

D = input()
s = input()

count = 0
a = 0
b = len(s)
while len(D)>=b:
    if s == D[a:b]:
        count += 1
        a=b
        b+=len(s)
    else:
        a+=1
        b+=1
print(count)