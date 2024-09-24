import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())


if N%2:
    print("SK")
else:
    print("CY")