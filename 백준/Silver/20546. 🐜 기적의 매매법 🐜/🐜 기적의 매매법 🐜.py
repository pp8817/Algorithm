import sys
input = lambda: sys.stdin.readline().rstrip()

money = int(input())
prices = list(map(int, input().split()))
BNP, TIMING = [money, 0], [money, 0] # 현급, 보유 주식 수
check_price = prices[0]
check = 0

for i, price in enumerate(prices):
    
    # BNP
    if BNP[0] >= price: 
        x = BNP[0]//price
        BNP[1] += x
        BNP[0] -= (x*price)

    if price > check_price: # 전일 대비 가격이 상승한다면
        if check > 0:
            check += 1
        else:
            check = 1

        if check == 3: # 3일 연속 가격 상승
            TIMING[0] += (TIMING[1]*price)
            TIMING[1] = 0
            check = 0

    elif price < check_price: # 전일 대비 가격이 하락한다면
        if check < 0:
            check -= 1
        else:
            check = -1
        if check == -3: # 3일 연속 하락
            x = TIMING[0]//price
            TIMING[1] += x
            TIMING[0] -= (x*price)
            check = 0

    else:
        check = 0

    check_price = price

BNP_assets = BNP[0] + BNP[1] * prices[-1]
TIMING_assets = TIMING[0] + TIMING[1] * prices[-1]

if BNP_assets > TIMING_assets:
    print("BNP")
elif BNP_assets < TIMING_assets:
    print("TIMING")
else:
    print("SAMESAME")