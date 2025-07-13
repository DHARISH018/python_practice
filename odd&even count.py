a=53467
odd=0
even=0
for num in str(a):
    if int(num)%2==0:
        even+=1
    else:
        odd+=1
print(odd)
print(even)