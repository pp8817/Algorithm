import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())

sol = [0]*(n+2)
sol[1], sol[2] = 1, 2
for i in range(3, n+1):
    sol[i] = (sol[i-2]+sol[i-1])%10007
print(sol[n])