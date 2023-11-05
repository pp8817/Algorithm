import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())

result_len = set()
result_len.add("ChongChong")

for _ in range(N):
    A, B = input().split()
    if (A in result_len) or (B in result_len):
        result_len.add(A)
        result_len.add(B)
print(len(result_len))