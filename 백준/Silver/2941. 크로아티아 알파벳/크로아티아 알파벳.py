S = input()

for i in ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]:
    if i in S:
        S = S.replace(i,".")
print(len(S))