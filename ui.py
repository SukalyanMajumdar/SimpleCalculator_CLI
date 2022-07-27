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

    while 1:
        val1 = input("\nInput Integer1: ")
        if calc.inputValidate2(val1) != 'go':
            print("\nInvalid Integer1 input, please retry")
        else:
            break

    while 1:
        val2 = input("\nInput Integer2: ")
        if calc.inputValidate2(val2) != 'go':
            print("\nInvalid Integer2 input, please retry")
        else:
            break

    result = calc.calculate(val1, val2, choice)

    print(result)

    reRunInput = input('''Press R to rerun the calculator
Press any other key to close the calculator
''')
    if reRunInput.lower() != 'r':
        break

print("Calculator Closing")
