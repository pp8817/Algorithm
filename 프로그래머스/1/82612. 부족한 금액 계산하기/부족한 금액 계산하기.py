def solution(price, money, count):
    index = 1
    temp = 0
    while count >= index :
        temp += (price * index)
        index += 1
    
    answer = temp - money
    return answer if answer > 0 else 0