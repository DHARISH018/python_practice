a = 123
reversed_num=0
while a>0:
    digit=a%10
    reversed_num=reversed_num*10+digit
    a=a//10
print(reversed_num)