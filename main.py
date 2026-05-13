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



def powerOf(numOne, numTwo):
    return str(float(numOne) ** float(numTwo))



def tokenize(equation, lastResult=""):
    num = lastResult
    tokens = []
    subToken = []

    for char in equation:
        if char in ["+", "-", "*", "/", "^"]:
            tokens.append(num)
            tokens.append(char)
            num = ""
        elif char.isdigit() or char == ".":
            num += char
        else:
            continue

    tokens.append(num)

    return tokens



def evaluate(listIn):
    operations = {
        "^": powerOf,
        "*": multiply,
        "/": divide,
        "+": add,
        "-": subtract,
    }

    tokens = listIn

    for operator in operations.keys():
        newTokens = [tokens[0]]
        for idx in range(1, len(tokens), 2):

            op = tokens[idx]
            right = tokens[idx + 1]

            if op == operator:
                left = newTokens.pop()
                result = operations[operator](left, right)
                newTokens.append(result)
            else:
                newTokens.append(op)
                newTokens.append(right)
        tokens = newTokens

    return newTokens[0]



def loadResult():
    try:
        with open("calcSave.txt", "r") as file:
            result = file.read()
            if result == "":
                result = None
            return result
    except FileNotFoundError:
        return None



def saveResult(result):
    with open("calcSave.txt", "w") as file:
        file.write(result)



# ~~~~~~~~~~~~~~~~~~~~~~~~~
# MAIN FUNCTION DEFINITION
# ~~~~~~~~~~~~~~~~~~~~~~~~~
def main():
    calcOn = True
    result = loadResult()

    while calcOn:
        useLastResult = False
        if result != None:
            print("")
            print("Use last result? (y/n)")
            print("")
            resultChoice = input(" --> ").lower()
            if resultChoice in ['yes', 'y']:
                useLastResult = True
            

        print("")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("")
        print("Enter an equation")
        print("")
        equation = input(" --> ")
        if useLastResult:
            tokens = tokenize(equation, result)
        else:
            tokens = tokenize(equation)

        result = evaluate(tokens)
        saveResult(result)

        print("")
        print(f" --> {result}")
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
