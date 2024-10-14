while 1:
    li = list(map(int, input().split()))
    if li[0] == 0:
        break
    b, p, m = li[0], li[1], li[2]
    n = int(str(p), b) % int(str(m), b)
    res = []
    while n >= b:
        res.append(str(n%b))
        n = n//b
    res.append(str(n))
    print(int(''.join(res[::-1])))