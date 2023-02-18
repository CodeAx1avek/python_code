num = int(input("Enter a three-digit integer: "))
originalNum = num
result = 0
while originalNum != 0:
    remainder = originalNum % 10
    result += remainder ** 3
    originalNum //= 10
if result == num:
    print(num, "is an Armstrong number.")
else:
    print(num, "is not an Armstrong number.")
