import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
end, sum, count = 0, 0, 0

    
for start in range(0, n):
    while sum < n and end < n :
        sum += end+1
        end += 1
    if sum == n:
        count += 1
    sum -= start+1
print(count)