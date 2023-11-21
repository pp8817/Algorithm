import sys
input = lambda: sys.stdin.readline().rstrip()


N = int(input())
score = []
for i in range(N):
    score.append(int(input()))
    
score.sort()
b=0
for i in range(1, len(score)+1):
    b += abs(score[i-1] - i)
print(b)