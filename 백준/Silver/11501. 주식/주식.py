T = int(input())
for _ in range(T):
    N = int(input())
    prices = list(map(int, input().split()))
    max_price = 0
    result = 0
        
    for i in range(N-1, -1, -1):
        price = prices[i]
        if price > max_price:
            max_price = price
        else:
            result += (max_price-price)
                
    print(result)