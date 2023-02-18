def factorial(n):
    factorial = 1
    if n<0:
        print('Error! Factorial of a negative number does"nt exit')
    else:
        for i in range(1,n+1):
            factorial *=i
        print(factorial)
factorial(4)


# n = int(input("Enter a positive integer: "))
# factorial = 1

# if n < 0:
#     print("Error! Factorial of a negative number doesn't exist.")
# else:
#     for i in range(1, n+1):
#         factorial *= i
#     print("Factorial of", n, "=", factorial)
