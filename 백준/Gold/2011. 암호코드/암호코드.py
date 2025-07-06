import sys
input = lambda: sys.stdin.readline().rstrip()

s = input()

if not s or s[0] == "0":
    print(0)
else:
    N = len(s)

    dp = [0]*(N+1)
    dp[0] = 1
    dp[1] = 1
    for i in range(2, N+1):
        one_digit = int(s[i-1]) # 마지막 한 자리
        two_digit = int(s[i-2:i]) # 마지막 두 자리

        if 1 <= one_digit <= 9:
            dp[i] += dp[i-1]

        if 10 <= two_digit <= 26:
            dp[i] += dp[i-2]

    print(dp[N]%1000000)