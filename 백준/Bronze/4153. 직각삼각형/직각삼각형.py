import sys
input = lambda: sys.stdin.readline().rstrip()

while True:
    li= list(map(int, input().split()))
    li = sorted(li)
    a, b, c = li[0], li[1], li[2]

    if a == b == c == 0:
        break
    if (a**2 + b**2) == c**2:
        print("right")
    else:
        print("wrong")