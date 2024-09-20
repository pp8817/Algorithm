import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
solvent = list(map(int, input().split())) # 오름차순

left_index, right_index = 0, N-1

ans_left, ans_right = left_index,right_index

ans = abs(solvent[0] + solvent[N-1])

while left_index < right_index:
    tmp = solvent[left_index] + solvent[right_index]

    if abs(tmp) < ans:
        ans_left, ans_right = left_index, right_index
        ans = abs(tmp)

        if ans == 0:
            break

    if tmp < 0: # 음수의 절대값이 더 크기 때문에 음수를 작게 해야함
        left_index += 1
    else: # 양수의 절대값이 더 크기 때문에 양수를 작게 해야함
        right_index -= 1


print(solvent[ans_left], solvent[ans_right])