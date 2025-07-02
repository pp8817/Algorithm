import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())

ans = 0
flowers = []
for _ in range(N):
    sm, sd, em, ed = list(map(int, input().split()))
    
    # 날짜를 '월*100+일'로 변환하여 정수 처리
    flowers.append([sm*100+sd, em*100+ed])

# 피는 날 오름차순 -> 지는 날 내림차순
## 같은 날 피는 꽃을 중 오래 피는 꽃을 먼저 선정하기 위해
flowers.sort(key=lambda x: (x[0], -x[1]))

start,end  = 301, 1130
i, count, max_end = 0, 0, 0

while start <= end:
    found = False

    while i < N and flowers[i][0] <= start:
        if flowers[i][1] > max_end:
            max_end = flowers[i][1]
            found = True
        
        i += 1
    
    if not found:
        print(0)
        exit()

    start = max_end
    count += 1

print(count)