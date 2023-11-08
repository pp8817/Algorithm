import sys
input = lambda: sys.stdin.readline().rstrip()
h,m,s = map(int,input().split())
sec = int(input())

s1 = (s+sec)%60
m1 = (s+sec)//60
m2 = (m+m1)%60
h1 = (m+m1)//60

h2 = (h+h1)%24 

print(h2,m2,s1) 