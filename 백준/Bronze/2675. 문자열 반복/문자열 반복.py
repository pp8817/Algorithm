T = int(input())

for _ in range(T):
    R, S = input().split()
    n = ""
    R = int(R)
    for i in S:
        n += i*R
    print(n)