import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
used_key = set()
for _ in range(N):
    option_str = input()
    words = option_str.split()

    found = False

    for i in range(len(words)):
        first_char = words[i][0].upper()
        if first_char not in used_key:
            used_key.add(first_char)
            words[i] = "["+words[i][0]+"]" + words[i][1:]

            print(" ".join(words))
            found = True
            break
    
    if found:
        continue

    result_chars = list(option_str)
    for i in range(len(result_chars)):
        char = result_chars[i]
        if char == " ": continue

        char_upper = char.upper()

        if char_upper not in used_key:
            used_key.add(char_upper)
            result_chars[i] = "["+char+"]"

            print("".join(result_chars))
            found=True
            break
    
    if not found:
        print(option_str)