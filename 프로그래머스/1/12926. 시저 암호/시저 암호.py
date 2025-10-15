def solution(s, n):
    answer = ""
    for ch in s:
        if ch == " ":
            answer += ch
            continue

        num = ord(ch) + n

        if 97 <= ord(ch) <= 122:
            if num > 122:
                num -= 26
                
        elif 65 <= ord(ch) <= 90:
            if num > 90:
                num -= 26

        answer += chr(num)

    return answer