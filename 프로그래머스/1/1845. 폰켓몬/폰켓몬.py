def solution(nums):
    answer = 0
    N = len(nums)
    maps = {}
    for i in range(N):
        num = nums[i]
        if num in maps:
            maps[num] += 1
        else:
            maps[num] = 1
    
    if len(maps) >= (N/2):
        answer = N/2
    else:
        answer = len(maps)
            
    return answer