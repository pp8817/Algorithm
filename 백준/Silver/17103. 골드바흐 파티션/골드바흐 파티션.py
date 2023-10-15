import sys
input = lambda: sys.stdin.readline().rstrip()
prime = []
check = [0] * 1000001
check[0] = 1
check[1] = 1

for i in range(2, 1000001):
    if check[i] == 0:
        prime.append(i)
        for j in range(2*i, 1000001, i):
            check[j] = 1

T = int(input())

for _ in range(T):
    count = 0
    N = int(input())
    for i in prime:
        if i >= N: # 소수 값이 N을 넘는다면 종료
            break
        if (not check[N - i]) and (i <= N-i):  # N보다 작은 Prime의 소수를 N에서 뺀 값도 소수라면 count += 1
            count += 1
    print(count)