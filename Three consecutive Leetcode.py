a = [1, 2, 3,5, 41, 15, 6]
k = int(input())

for i in range(len(a) - k + 1):
    if all(a[i + j] % 2 == 1 for j in range(k)):
        print(f"Found {k} consecutive odd numbers starting from index {i}: {a[i:i+k]}")
        break
else:
        print("not found")