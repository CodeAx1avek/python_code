def result(N):
    for num in range(N):
        if num % 3 == 0 and num % 5 == 0:
            print(num, end=" ")


if __name__ == "__main__":
    N = 100
    result(N)
