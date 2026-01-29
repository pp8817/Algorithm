import sys
input = lambda: sys.stdin.readline().rstrip()

sound = list(input())
N = len(sound)

order = {'q': 0, 'u': 1, 'a': 2, 'c': 3, 'k': 4}
ducks = []

answer = 0

for ch in sound:
    idx = order[ch]
    found = False

    for i in range(len(ducks)):
        if ducks[i] == idx-1:
            ducks[i] = idx
            found = True
            break
    
    if not found:
        if ch == "q":
            ducks.append(0)
            answer = max(answer, len(ducks))
        else:
            print(-1)
            exit()
    
    if ch == "k":
        ducks.remove(4)

if ducks:
    print(-1)
else:
    print(answer)