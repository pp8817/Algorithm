def solution(s):
    maps = {
        "zero": "0", "one": "1", "two": "2", "three": "3", "four": "4",
        "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"
    }
    number = set("0123456789")
    temp = ""
    answer = ""

    for ch in s:
        if ch in number:
            answer += ch
        else:
            temp += ch
            if temp in maps:
                answer += maps[temp]
                temp = ""
    return int(answer)