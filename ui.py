import calc

print("\nWelcome to Calculator\n")

while 1:

    choice = "default"

    while 1:
        print('''Enter choice:
1. Addition
2. Subtraction
3. Multiplication
4. Division''')
        choice = input('Select any operation: ')
        nextStep = calc.inputValidate(choice)
        if nextStep != 'go':
            print("\nInvalid choice, please retry\n")
        else:
            break

    val1 = input("\nInput Integer1: ")
    val2 = input("Input Integer2: ")

    result = calc.calculate(val1, val2, choice)

    print(result)

    reRunInput = input('''Press R to rerun the calculator
Press any other key to close the calculator
''')
    if reRunInput.lower() != 'r':
        break

print("Calculator Closing")
