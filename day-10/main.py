def plus(num1,num2):
    return num1 + num2

def minus(num1,num2):
    return num1 - num2

def multiply(num1,num2):
    return num1*num2

def divide(num1,num2):
    return num1/num2

def calculator(num1, num2, operation):
    if operation == '+':
        return plus(num1,num2)
    elif operation == '-':
        return minus(num1,num2)
    elif operation == '*':
        return multiply(num1,num2)
    elif operation == '/':
        return divide(num1,num2)
    else:
        raise Exception('Invalid operation')

def main():

    control = 'n'
    while True:

        if control == 'n':
            num1 = float(input("What's the first number?: "))
        else: 
            num1 = result

        print('+\n-\n*\n/')
        operation = input('Pick an operation: ')

        num2 = float(input("What's the next number?: "))

        result = calculator(num1,num2,operation)

        print("{:.2f} {} {:.2f} = {:.2f}".format(num1,operation,num2,result))

        control = input("Type 'y' to continue calculating with {:.2f}, or type 'n' to start a new calculation:".format(result))



main()