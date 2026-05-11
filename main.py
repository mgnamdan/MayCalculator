# ~~~~~~~~~~~~~~~~~~~~~~~~~
# HELPER FUNCTIONS AND IMPORTS
# ~~~~~~~~~~~~~~~~~~~~~~~~~
def add(numOne, numTwo):
    return numOne + numTwo



def subtract(numOne, numTwo):
    return numOne - numTwo



def multiply(numOne, numTwo):
    return numOne * numTwo



def divide(numOne, numTwo):
    try:
        return numOne / numTwo
    except ZeroDivisionError:
        return 0



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
    operations = {"+": add,
                  "-": subtract,
                  "*": multiply,
                  "/": divide}
    
    newChunks = []
    for idx in range(len(tokens)):
        if tokens[idx] == operator:
            numOne = float(tokens[idx-1])
            numTwo = float(tokens[idx+1])
            result = operations[operator](numOne, numTwo)
            newChunks.append(result)
        elif tokens[idx] != operator and tokens[idx] in ["+", "-", "*", "/"]:
            newChunks.append(tokens[idx-1])
            newChunks.append(tokens[idx])
            newChunks.append(tokens[idx+1])
        else:
            continue

    return newChunks



# ~~~~~~~~~~~~~~~~~~~~~~~~~
# MAIN FUNCTION DEFINITION
# ~~~~~~~~~~~~~~~~~~~~~~~~~
def main():
    calcOn = True

    

    while calcOn:
        print("")
        print("Would you like to perform another operation? (y/n)")
        print("")
        goAgain = input(" --> ").lower()
        if goAgain in ["no", "n", "exit", "quit"]:
            calcOn = False

        elif goAgain in ["yes", "y"]:
            # Do some calculating
            print("~~~~~~~~~~~~~~~~~~~~")
            print("")
            print("Enter an equation (ex. '2 + 2 - 4)")
            print("")
            equation = input(" --> ")
            chunks = tokenize(equation)

            chunks = evaluate(chunks, "*")
            print(chunks)
            chunks = evaluate(chunks, "/")
            print(chunks)
            chunks = evaluate(chunks, "+")
            print(chunks)
            chunks = evaluate(chunks, "-")
            print(chunks)




        else:
            print("Invalid option - choose again!")


    # userInput = input("Type in an operation: +, - ,* /")
    # numOne = input("Give me a number")
    # numTwo = input("Give me another number")
    # operations["+"] # --> add
    # operations["+"](numOne, numTwo) # --> add(numOne, numTwo)
    # operations[userInput](numOne, numTwo)


# ~~~~~~~~~~~~~~~~~~~~~~~~~
# MAIN FUNCTION CALL
# ~~~~~~~~~~~~~~~~~~~~~~~~~
main()
