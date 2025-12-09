from collections import Counter
import sys
input = sys.stdin.readline

a = input().rstrip()
b = input().rstrip()

ca = Counter(a)
cb = Counter(b)

ans = 0
for ch in set(ca.keys()) | set(cb.keys()):
    ans += abs(ca[ch] - cb[ch])

print(ans)