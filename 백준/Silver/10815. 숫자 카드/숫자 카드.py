import sys
n = int(sys.stdin.readline())
arr1 = set(map(int, sys.stdin.readline().split()))

m = int(input())
arr2 = list(map(int, sys.stdin.readline().split()))

for i in arr2:
    k=0
    if i in arr1:
        k = 1
    print(k, end=' ')