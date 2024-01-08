import sys
input = lambda: sys.stdin.readline().rstrip()

A, B = map(int, input().split())
count = 0

while A!=B:
    if A>B:
      count=-2
      break
    elif str(B)[-1]=='1':
        count += 1
        B = B//10
    elif (B%2) == 0:
        count += 1
        B = B//2
    else:
      count=-2
      break
print(count+1)