N = int(input("Enter the N value:"))
Oddsum = 0
Evensum = 0

for i in range(1, N+1):
    if i%2 != 0:
        Oddsum += i
    else:
        Evensum += i
print("Sum of the odd numbers", Oddsum, "and sum of the even numbers", Evensum)