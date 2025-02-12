def solution(prices):
    answer = [0]*len(prices)
    N = len(prices)
    for i in range(N):
        time = 0
        price = prices[i]
        for j in range(i+1, N):
            time += 1
            if price > prices[j]:
                break
        answer[i] = time
    return answer