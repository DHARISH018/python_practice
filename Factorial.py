n = int(input("Enter the number: "))

if n == 0:
    print(False)
else:
    i = 2
    original = n
    while n % i == 0:
        n = n // i
        i += 1

    if n == 1:
        print("It's a factorial number.")
    else:
        print("Not a factorial number.")
