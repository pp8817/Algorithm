while True:
    a, b, c = map(int,input().split())
    li = [a,b,c]
    li.sort()

    if a==b==c==0:
        break
    elif li[2] >= li[0] + li[1]:
        print("Invalid")
    elif a==b==c:
        print("Equilateral")
    elif a==b or a==c or b==c:
        print("Isosceles")
    else: 
        print("Scalene")