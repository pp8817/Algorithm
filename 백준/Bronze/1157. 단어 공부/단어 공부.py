word = input().upper()
word_set = list(set(word))
c_list = []

for i in word_set:
    c = word.count(i)
    c_list.append(c)
if c_list.count(max(c_list))>1:
    print('?')
else:
    max_index = c_list.index(max(c_list))
    print(word_set[max_index])

