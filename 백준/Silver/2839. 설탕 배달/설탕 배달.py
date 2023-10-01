a = int(input())
box = 0
while True:
  if a%5 ==0:
    box = box + (a//5)
    print(box)
    break
  a = a - 3
  box += 1
  if a < 0:
    print("-1")
    break