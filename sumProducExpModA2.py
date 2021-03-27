# Name: Orion Assefaw, COMP517 Assignment 2

# mainMenu()- Gives User 5 options to choose from
# Takes user input(string) by prompting user to type in their option
# Returns - a float of the sum , product or modulo of two numbers
#           or an int of the exponentiation; depending on user choices
def mainMenu():
    menu = input("Welcome!! Please select one of the following options :\n 1- For Addition(Summation) \n 2- For Multiplication \n 3- For Exponentiation \n 4- For Modulo calculation \n q- To exit the program \n")

    # Option 1 Calculates the sum of two numbers inputed by the user and prints the result out
    if (menu == "1"):
        x = float(input("Enter the first number please  : "))
        y = float(input("Enter the second number please : "))
        print("The sum of", x, "and", y, "is :", sum(x, y))
        print("Thank you for using the program")
        print("You will once again be redirected to the Main Menu where you can choose to quit or continue with the operations \n")
        mainMenu()

    # Option 2 Calculates the product of two numbers inputed by the user and prints the result out
    elif (menu == "2"):
        x = float(input("Enter the first number please : "))
        y = int(input("Enter the second number please : "))
        print("The product of", x, "and", y, "is :", prod(x, y))
        print("Thank you for using the program")
        print("You will once again be redirected to the Main Menu where you can choose to quit or continue with the operations \n")
        mainMenu()

    # Option 3 Calculates the exponentiation of two numbers inputed by the user(first number to the power of second)
    # and prints the result out
    elif (menu == "3"):
        x = int(input("Enter the first number please : "))
        y = int(input("Enter the second number please : "))
        print(x, "to the power of", y, "(X^y) is therefore : ", exp(x, y))
        print("Thank you for using the program")
        print("You will once again be redirected to the Main Menu where you can choose to quit or continue with the operations \n")
        mainMenu()

    # Option 4 Calculates the mdulo of two numbers inputed by the user(first number inputed modulo the second number)
    # and prints the result out
    elif (menu == "4"):
        x = float(input("Enter the first number please : "))
        y = float(input("Enter the second number please : "))
        print(x, "modulo", y, "is therefore : ", modulo(x, y))
        print("Thank you for using the program")
        print("You will once again be redirected to the Main Menu where you can choose to quit or continue with the operations \n")
        mainMenu()

    # This option lets the user exit the program
    elif(menu == "q"):
        raise SystemExit

    # This is ivalid input check. If the user's input is none of the above five options, the user gets an error message
    # and is made to return to the main menu again
    else:
        print("Oops!! Invalid Input! Please try again to enter a valid input \n")
        mainMenu()


# sum(x, y) – calculates the sum of x and y
# Parameters: x – float , y - float
# Returns: float – the calculated sum
def sum(x, y):
    return x + y
    

# prod(x, y) – calculates the product of x and y
# Parameters: x – float , y - int , (both positive numbers)
# Returns: float – the calculated product
def prod(x, y):
    # Positive Input check
    if (x > 0 and y > 0):
        product = 0
        for i in range(0, y):
            product = sum(product,x)
        return product
    # In case of invalid input
    else:
        print("You can not input zero and/or negative values, please retry by entering positive numbers only")
        mainMenu()


# exp(x, y) – calculates the exponentiation of x to the power of y
# Parameters: x – int , y-int , (both positive numbers)
# Returns: int – the calculated exponentiation
def exp(x, y):
    # Positive Input check
    if (x > 0 and y > 0):
        expResult = x
        counter = sum(y,-1)
        while (counter > 0):
            expResult = prod(expResult, x)
            counter = sum(counter,-1)
        return expResult
    # In case of invalid input
    else:
        print("You can not input zero and/or negative values, please retry by entering positive numbers only")
        mainMenu()
    

# modulo(x, y) – calculates x modulo y
# Parameters: x – float , y - float , (both positive numbers)
# Returns: float – the calculated modulo
def modulo(x, y):
    # Positive Input check
    if (x > 0 and y > 0):
        moduloResult = x
        while (sum(moduloResult, -y) >= 0):
            moduloResult = sum(moduloResult, -y)
        return moduloResult
    # In case of invalid input    
    else:
        print("You can not input zero and/or negative values, please retry by entering positive numbers only")
        mainMenu()


# Program Initiator
mainMenu()