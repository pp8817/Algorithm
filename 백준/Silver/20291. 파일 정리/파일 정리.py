import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input()) # 1<=N<=50000
extension = dict()

for _ in range(N):
    name, ext = input().split(".")
    if ext in extension:
        extension[ext] += 1
    else:
        extension[ext] = 1

extension = sorted(extension.items())

for ext in extension:
    print(*ext)