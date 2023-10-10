import sys
input = lambda: sys.stdin.readline().rstrip()
s = input()
arr = set()
for i in s:
    arr.add(i)
for i in range(len(s)):
    for j in range(i+1, len(s)):
        arr.add(s[i]+s[i+1:j+1])
print(len(arr))