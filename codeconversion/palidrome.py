num  = int(input("Enter The Positive Number:"))
n = num
rev = 0
while num != 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10
print('The Reverse is: ',rev)
if n == rev:
    print("IT IS PALIDROME NUMBER")
else:
    print("IT IS NOT PALIDROME NUMEBR")