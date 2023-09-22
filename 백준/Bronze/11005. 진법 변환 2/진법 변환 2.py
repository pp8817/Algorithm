N, B = map(int, input().split())
ans=""
while N:
    b = N%B
    N = N//B
    if b<10:
        ans+=str(b)
    else:
        ans+=chr(ord("A")+b-10)
print(ans[::-1])


# N, B = map(int, input().split())
# li = []

# while N>0:
#     b = N%B
#     N = N//B
#     li.append(b)

# li.reverse()
# for i in li:
#     if i<10:
#         print(i, end="")
#     else:
#         print(chr(i+55), end="")
