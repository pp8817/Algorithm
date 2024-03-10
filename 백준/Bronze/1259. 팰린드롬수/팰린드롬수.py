import sys
input = lambda: sys.stdin.readline().rstrip()

while True:
    st = input()

    if st == '0':
        break

    st = list(st)

    l = len(st)//2
    a = st[:l]
    if len(st)%2==0:
        b = st[l:][::-1]
    else:
        b = st[l+1:][::-1]
    if a == b:
        print("yes")
    else:
        print("no")