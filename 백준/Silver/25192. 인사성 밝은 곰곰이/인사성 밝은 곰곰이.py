import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())

s = set() 
count = 0
for _ in range(N):
    inp = input()
    
    if inp == "ENTER":
        count += len(s)
        s.clear()
    else:
        s.add(inp)
count += len(s)
print(count)