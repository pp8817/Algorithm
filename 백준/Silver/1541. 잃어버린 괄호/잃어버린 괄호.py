import sys
input = lambda: sys.stdin.readline().rstrip()

formula = list(input().split('-'))
ls_formula = []
ans = 0
for i in range(len(formula)):
    ls = list(map(int, formula[i].split('+')))
    if i == 0:
        ans += sum(ls)
    else:
        ans += -sum(ls)
    ls_formula.append(ans)

print(ans)