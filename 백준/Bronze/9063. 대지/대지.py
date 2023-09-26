n = int(input())
li_x = []
li_y = []
for i in range(n):
    x, y = map(int, input().split())
    li_x.append(x)
    li_y.append(y)
if n == 1:
    print(0)
else:
    print((max(li_x)-min(li_x))*(max(li_y)-min(li_y)))