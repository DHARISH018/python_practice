a="361589"
b=""
counts=0
c=''
even=0
for i in a:
    if int(i)%2!=0:
        b+=i
        counts=len(b)

    else:
        c+=i
    even=len(c)

print(b+str(counts)+c+str(even))
