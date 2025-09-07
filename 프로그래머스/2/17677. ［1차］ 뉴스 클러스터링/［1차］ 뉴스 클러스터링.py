from collections import Counter

def solution(str1, str2):
    answer = 0

    arr1, arr2 = [], []
    for i in range(len(str1)-1):
        ch1, ch2 = str1[i].lower(), str1[i+1].lower()
        if ch1.isalpha() and ch2.isalpha():
            arr1.append(ch1+ch2)
            
    for i in range(len(str2)-1):
        ch1, ch2 = str2[i].lower(), str2[i+1].lower()
        if ch1.isalpha() and ch2.isalpha():
            arr2.append(ch1+ch2)
            
    cnt1, cnt2 = Counter(arr1), Counter(arr2)
    keys = set(cnt1) | set(cnt2)
    
    inter = sum(min(cnt1[k], cnt2[k]) for k in keys)
    union = sum(max(cnt1[k], cnt2[k]) for k in keys)
    
    if union == 0:
        return 65536
    
    return int((inter / union)*65536)