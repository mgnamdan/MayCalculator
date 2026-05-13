# ~~~~~~~~~~~~~~~~~~~~~~~~~
# HELPER FUNCTIONS AND IMPORTS
# ~~~~~~~~~~~~~~~~~~~~~~~~~
def add(numOne, numTwo):
    return str(float(numOne) + float(numTwo))



def subtract(numOne, numTwo):
    return str(float(numOne) - float(numTwo))



def multiply(numOne, numTwo):
    return str(float(numOne) * float(numTwo))



def divide(numOne, numTwo):
    try:
        return str(float(numOne) / float(numTwo))
    except ZeroDivisionError:
        print("An error occurred - unable to divide by zero in the equation")
        return "Error"



def tokenize(equation):
    num = ""
    tokens = []

    for char in equation:
        if char in ["+", "-", "*", "/"]:
            tokens.append(num)
            tokens.append(char)
            num = ""
        elif char.isdigit() or char == ".":
            num += char
        else:
            continue

    tokens.append(num)

    return tokens



def evaluate(tokens, operator):
    operations = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide,
    }

    newTokens = [tokens[0]]

    for idx in range(1, len(tokens), 2):
    
        # [2, +, 4, +, 5]

        op = tokens[idx]
        right = tokens[idx + 1]

        if op == operator:
            left = newTokens.pop()
            result = operations[operator](left, right)
            newTokens.append(result)
        else:
            newTokens.append(op)
            newTokens.append(right)

    return newTokens



# ~~~~~~~~~~~~~~~~~~~~~~~~~
# MAIN FUNCTION DEFINITION
# ~~~~~~~~~~~~~~~~~~~~~~~~~
def main():
    calcOn = True

    while calcOn:

        print("")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("")
        print("Enter an equation")
        print("")
        equation = input(" --> ")

        tokens = tokenize(equation)
        for operator in ['*', '/', '+', '-']:
            tokens = evaluate(tokens, operator)

        print("")
        print(f" --> {tokens[0]}")
        print("")

        print("")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Would you like to perform another operation? (y/n)")
        print("")
        validChoice = False
        while not validChoice:
            goAgain = input(" --> ").lower()
            if goAgain in ["no", "n", "exit", "quit"]:
                calcOn = False
                validChoice = True
            elif goAgain in ["yes", "y"]:
                validChoice = True
            else:
                print("Invalid option - choose again!")



# ~~~~~~~~~~~~~~~~~~~~~~~~~
# MAIN FUNCTION CALL
# ~~~~~~~~~~~~~~~~~~~~~~~~~
main()
