def arithmeticMean(arr, n):
    sum = 0
    for i in range(n):
        sum += arr[i]
    am = sum / n
    return am

n = int(input("Enter the Size (max. 3 number): "))
arr = []
print("\nEnter", n, "Numbers: ")
for i in range(n):
    arr.append(float(input()))

armean = arithmeticMean(arr, n)
print("\nArithmetic Mean = ", armean)
