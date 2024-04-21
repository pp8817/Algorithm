N = int(input())

for _ in range(N):
    num = int(input())
    k = len(str(num)) #주어진 숫자가 몇자리 숫자인지를 확인합니다
    if str(num**2)[-k:] == str(num): #제곱수를 뒤에서 sli만큼만 가져와 num과 동일한지 판단합니다
        print("YES")
    else:
        print("NO")
