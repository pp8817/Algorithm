def solution(name, yearning, photo):
    name_dic = {i:v for i, v in zip(name, yearning)}
    
    photo_len = len(photo)
    
    answer=[0]*photo_len
    for i in range(photo_len):
        count = 0
        for name in photo[i]:
            if name in name_dic:
                count += name_dic[name]        
        answer[i] = count
    return answer