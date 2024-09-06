answer = 0
def solution(N, number):
    # s[i]: N을 i번 사용해서 만들 수 있는 수들의 집합
    s = [set() for _ in range(8)] #range(8)인 이유: N을 8번보다 많이 사용하면 -1 리턴
    
    for i, x in enumerate(s, start=1):
        x.add(int(str(N)*i))
        
    for i in range(len(s)): # N들을 i번 사용해서 만들 수 있는 숫자들을 구할 예정
        for j in range(i): # i: 2인 경우, j: 0,1
            for op1 in s[j]: # op1: 피연산자1, N을 j+1번 사용해서 만들 수 있는 숫자들
                for op2 in s[i-j-1]: # op2: 피연산자2, N을 (i-j)번 사용해서 만들 수 있는 숫자들
                    s[i].add(op1+op2)
                    s[i].add(op1-op2)
                    s[i].add(op1*op2)
                    
                    if op2 != 0 and (op1>=op2):
                        s[i].add(op1//op2)
        if number in s[i]: # 찾고자 하는 수 number가 s[i]에 존재한다면
            answer = i+1
            return answer
        
    return -1
