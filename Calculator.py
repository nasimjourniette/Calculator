from xml.etree.ElementTree import TreeBuilder


def main():
    # add a loop to continue calculations
    more_operations = True
    while more_operations:
        try:
            # if num1 does not exist, an UnboundLocalError will be raised and the user can assign num1 to a number.
            # it's to restart the whole loop after the user is done with their certain calculation and wants to start a new one
            # else they are continuing with a calculation from a result of one of their previous calculations
            if num1 != None:
                print(f"Your first number is {num1}")
        except UnboundLocalError:
            # both numbers can have a factorial symbol after to represent a factorial
            while True:
                try:
                    num1 = input("What's your first number? ")
                    if num1[:-1].isnumeric and num1[-1] == '!' or num1.isnumeric():
                        pass
                    else:
                        raise ValueError
                except ValueError:
                    print('please type a valid number')
                else:
                    break
        # let user give a valid operation
        while True:
            try:
                operation = input("What operation are you using on this number? ")
                if operation not in ('+', '-', '*', '^', '/', '**'):
                    print('Not a valid operation.')
                    raise ValueError
            except ValueError:
                pass
            else:
                break
        while True:
            try:
                num2 = input("What number will you operate with? ")
                if num2[:-1].isnumeric and num2[-1] == '!' or num2.isnumeric():
                    pass
                else:
                    raise ValueError
            except ValueError:
                print('please type a valid number')
            else:
                break
        # if a number has a factorial sign then for each number from 1 up to the inputted number multiply it
        if '!' == num1[-1]:
            fact = 1
            for factorial in range(1, int(num1[:-1]) + 1):
                fact *= factorial
            num1 = fact
        
        if '!' == num2[-1]:
            fact2 = 1
            for factorial in range(1, int(num2[:-1]) + 1):
                fact2 *= factorial
            num2 = fact2
        # use the inputted information to find the result of the two numbers
        result = float(operate(num1, operation, num2)) 
        print(f'{num1} {operation} {num2} = {result}')
        # ask user to decide whether to start with brand new numbers, start with the result, or quit
        while True:
            try:
                again = input(f'Would you like to continue operating with {result}: ("yes", "y") or start a new calculation: ("no", "n") or quit: ("Ctrl + C") ').lower()
                if again in ('y','yes','no','n'):
                    if again in ('y', 'yes'):
                        num1 = str(result)
                    elif again in ('no', 'n'):
                        # delete num1 one so when the loop starts again, the UnboundLocalError triggers.
                        del num1
                else:
                    raise ValueError
            except KeyboardInterrupt:
                quit()
            except ValueError:
                print(f"Type one of these: {'y','yes', 'no', 'n'}.")
            else:
                break


def operate(n1, operand, n2):
    n1, n2 = float(n1), float(n2)
    if operand == '+':
        return n1 + n2
    elif operand == '-':
        return n1 - n2
    elif operand == '*':
        return n1 * n2
    elif operand == '/':
        return n1 / n2
    elif operand == '^' or operand == '**':
        return n1 ** n2


if __name__ == '__main__':
    main()
