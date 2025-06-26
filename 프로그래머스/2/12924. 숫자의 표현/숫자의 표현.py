def solution(n):
    count = 0
    for k in range(1, n + 1):
        if (n - (k * (k - 1)) // 2) <= 0:
            break
        if (n - (k * (k - 1)) // 2) % k == 0:
            count += 1
    return count