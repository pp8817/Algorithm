# 브루트포스 알고리즘
import sys
input = lambda: sys.stdin.readline().rstrip()

pre = 100
N = int(input())
int(input())
broken = list(map(int, input().split()))

# 현재 채널에서 +, -만 사용해서 이동할 경우
answer = abs(100-N)

for nums in range(1000001):
    nums = str(nums)

    for i in range(len(nums)):
        if int(nums[i]) in broken: #각 숫자가 고장난 버튼에 속하는지 검증
            break
        elif i == len(nums)-1: # 고장난 버튼이 없다면
            answer = min(answer, abs(int(nums) - N) + len(nums))
print(answer)