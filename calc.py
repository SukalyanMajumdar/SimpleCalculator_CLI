def inputValidate(inputVal):
    valid_choices = ["1", "2", "3", "4"]

    if (inputVal in valid_choices):
        return 'go'
    else:
        return None


def inputValidate2(inputVal):
    try:
        int(inputVal)
        return 'go'
    except ValueError:
        return None
    

    # if (inputVal.isdigit()):
    #     return 'go'
    # else:
    #     return None


def add(var1, var2):
    return int(var1) + int(var2)


def sub(var1, var2):
    return int(var1) - int(var2)


def mult(var1, var2):
    return int(var1) * int(var2)


def div(var1, var2):
    return int(var1) / int(var2)


def calculate(var1, var2, operation):
    funcs = [add, sub, mult, div]

    if var2 == "0" and operation == "4":
        return "\nCan not divide by Zero\n"
    else:
        answer = funcs[int(operation) - 1](var1, var2)
        return "\nResult is: " + str(answer) + "\n"
