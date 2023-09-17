array = [list(map(int, input().split())) for _ in range(9)]
num = 0
row, col = 0, 0
for i in range(9):
  for j in range(9):
    if num <= array[i][j]:
      row = i + 1
      col = j + 1
      num = array[i][j]
print(num)
print(row, col)