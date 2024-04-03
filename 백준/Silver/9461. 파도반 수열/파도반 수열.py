import sys
input = lambda: sys.stdin.readline().rstrip()

answer = [0]*105
answer[1], answer[2], answer[3] = 1, 1, 1

for i in range(4, len(answer)):
    answer[i] = answer[i-2]+answer[i-3]

for _ in range(int(input())):
    print(answer[int(input())])