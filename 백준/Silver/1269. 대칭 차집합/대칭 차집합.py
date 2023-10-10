import sys
input = lambda: sys.stdin.readline().rstrip()
n, m = map(int, input().split())
arr1 = set(list(map(int, input().split())))
arr2 = set(list(map(int, input().split())))
a = len(arr1 - arr2)
b = len(arr2 - arr1)
print(a+b)