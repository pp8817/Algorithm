def solution(wallet, bill):
    answer = 0
    row, col = wallet[0], wallet[1]
    bill.sort(); wallet.sort() # bill[1], wallet[1]가 항상 큰 값을 유지
    while True:
        if bill[1] <= wallet[1] and bill[0] <= wallet[0]:
            break
            
        bill[1] = bill[1]//2
        if bill[1] < bill[0]:
            bill[0], bill[1] = bill[1], bill[0]
        answer += 1
    return answer