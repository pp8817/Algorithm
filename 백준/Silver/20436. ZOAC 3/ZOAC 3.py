import sys
input = lambda: sys.stdin.readline().rstrip()

l, r = input().split()  # 양 손가락 시작 위치
str = input()

keyboard = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']
mo = 'yuiophjklbnm'
xl, yl, xr, yr = 0, 0, 0, 0

for i in range(len(keyboard)):
    if l in keyboard[i]:
        xl, yl = i, keyboard[i].index(l)

    if r in keyboard[i]:
        xr, yr = i, keyboard[i].index(r)

ans = 0
for s in str:
    ans += 1

    if s in mo:
        for i in range(3):
            if s in keyboard[i]:
                nx = i
                ny = keyboard[i].index(s)

                ans += abs(xr-nx) + abs(yr-ny)

                xr, yr = nx, ny
                break
    else:
        for i in range(3):
            if s in keyboard[i]:
                nx = i
                ny = keyboard[i].index(s)

                ans += abs(xl-nx) + abs(yl-ny)

                xl, yl = nx, ny
                break

print(ans)