a=input()
word=""
for ch in range(len(a)-1,-1,-1):
    word+=a[ch]
print(word)