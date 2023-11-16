N = int(input("Enter the people numbers: "))
i = 1
sum = 0
while i <= N:
    sum = int(((N * (N - 1)) / 2))
    i += 1
print(sum)