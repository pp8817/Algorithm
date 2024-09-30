import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
limit_w = list(map(int, input().split())) # 크레인 무게 제한
M = int(input())
W = list(map(int, input().split()))

limit_w.sort(reverse=True)
W.sort(reverse=True)
ans = 0

if W[0] > limit_w[0]: ans=-1
else:
    while W:
        for c in limit_w:
            if W and c < W[-1]:
                break
            for w in W:
                if c >= w:
                    W.remove(w)
                    break
        ans += 1

print(ans)