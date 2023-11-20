def solution(s):
    s = s.lower()
    li = s.split(" ")
    result =[]
    for st in li:
        if st == "":
            result.append("")
        else:
            if st[0].isalpha():
                result.append(st[0].upper() + st[1:])
            else:
                result.append(st)
    return " ".join(result)