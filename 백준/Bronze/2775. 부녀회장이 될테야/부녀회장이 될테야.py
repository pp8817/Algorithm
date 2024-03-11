import sys
input = lambda: sys.stdin.readline().rstrip()

T = int(input())
# sol: 가장 꼭대기에서 마지막 호는 14층 14호, 즉 0~14열, 0~14행에 해당하는 모든 호의 값을 그냥 구하고 빼는게 더 편할듯

result = [[0]*14 for _ in range(15)]

for i in range(0, 14):
    result[0][i] = i+1

for i in range(1, 15):
    for j in range(14):
        result[i][j] = sum(result[i-1][:j+1])
for _ in range(T):
    print(result[int(input())][int(input())-1])
