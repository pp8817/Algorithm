import sys
input = lambda: sys.stdin.readline().rstrip()

MOD = 1_000_000_000
n = int(input())

m = abs(n)

if m == 0:
    print(0)
    print(0)
else:
    a, b = 0, 1
    for _ in range(2, m + 1):
        a, b = b, (a + b) % MOD

    sign = 1 if n > 0 or n % 2 != 0 else -1
    print(sign)
    print(b % MOD)