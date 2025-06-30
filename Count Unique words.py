
a=("These is a map and learning python python is short and python easy ")
words=a.split()
word={}
for ch in words:
    if ch in word:
        word[ch]+=1
    else:
        word[ch]=1
for value in words:
    if word[value]==1:
        print(value)
