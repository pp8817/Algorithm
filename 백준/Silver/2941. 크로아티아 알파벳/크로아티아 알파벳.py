word = input()
a = ['c=','c-','dz=','d-','lj','nj','s=','z=']
for i in a:
    word = word.replace(i, '*')
print(len(word))