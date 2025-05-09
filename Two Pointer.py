arr= [1, 3, 4, 5, 7, 10, 11]
target=22
l=0
r=len(arr)-1
while (l<r):
    act=arr[l]+arr[r]
    if act==target:
        print(l,r)
        break
    elif act<target:
        l=l+1
    elif act>target:
        r=r-1
else:
    print('error')
