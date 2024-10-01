import sys
input = lambda: sys.stdin.readline().rstrip()
# 같은 원소가 K개 이하로 들어있는 최장 연속 부분 수열의 길이
N, K = map(int, input().split()) # 수열 길이, 정수 제한 갯수
arr = list(map(int, input().split()))

dict = {}
for i in arr:
    if i in dict:
        continue
    dict[i] = 0

start,end = 0,0

ans = 0
while end != N:
    x = arr[end]
    if dict[x] == K: # 이미 x의 갯수가 K와 같을시 x를 추가하면 문제가 됨.
        ans = max(ans, end-start)
        # start의 위치를 x가 처음나오는 위치까지 변경
        while True:
            if arr[start] == x:
                dict[x] -= 1
                start += 1
                break
            else:
                dict[arr[start]] -= 1
            start += 1

    elif dict[x] < K:
        dict[x] += 1
        end += 1

ans = max(ans, end-start)

print(ans)