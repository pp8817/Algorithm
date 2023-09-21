buf = [[0 for _ in range(100)] for _ in range(100)]

n = int(input())

for _ in range(n):
    x, y = map(int, input().split())
    for i in range(10):
        for j in range(10):
            buf[x+i-1][y+j-1] = 1
count = 0
for x in range(100):
    for y in range(100):
        count += buf[x][y]
print(count)