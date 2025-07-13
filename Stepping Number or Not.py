a=12345
b=str(a)
increasing=True
for num in  range(len(b) - 1):
    if int(b[num]) - int(b[num+1]) !=-1:
        increasing=False
        break
print("YES" if increasing else "NO")

