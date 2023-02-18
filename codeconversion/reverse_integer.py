n = int(input('Enter The Integer: '))
rev = 0
while n != 0:
    remainder = n % 10
    rev = rev * 10 + remainder
    n//=10
print('Your Reverse Integer is:',rev)