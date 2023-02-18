def calc(num1,num2):
    op = input('Enter The Operator: +,-,/,,*,%')
    if op == '+':
        result = num1+num2
        return  result
    elif op =='-':
        result = num1-num2
        return  result
    elif op == '*':
        result= num1*num2
        return  result
    elif op == '/':
        result = num1/num2
        return  result
    elif op == '%':
        result = num1%num2
        return  result
    else:
        print('Incorrect Operator!')
num1 = float(input('Enter the number1 :'))
num2 = float(input('Enter The number2 :'))
print(calc(num1,num2))
