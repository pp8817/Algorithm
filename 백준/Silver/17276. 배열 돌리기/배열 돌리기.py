import sys
input = lambda: sys.stdin.readline().rstrip()    

T = int(input())

for _ in range(T):
    n, d = map(int, input().split())
    arr = list(list(map(int, input().split())) for _ in range(n))

    middle = n//2
    if d > 0:
        cnt = d//45
    else:
        cnt = (360+d)//45

    # 시계 방향으로 처리하는 로직을 만들고 반시계 방향으로 들어오는 경우, 시계 360 - (d)만큼 처리
    for _ in range(cnt):
        # 주 대각선
        l1 = [arr[i][i] for i in range(n)]
        # 가운데 열
        l2 = [arr[i][middle] for i in range(n)]
        # 부 대각선
        l3 = [arr[n-1-i][i] for i in range(n)]
        # 가운데 행
        l4 = arr[middle][:]
        
        for i in range(n):
            arr[i][middle] = l1[i]
            arr[i][n-1-i] = l2[i]
            arr[middle][i] = l3[i]
            arr[i][i] = l4[i]
    
    for row in arr:
        print(' '.join(map(str, row)))