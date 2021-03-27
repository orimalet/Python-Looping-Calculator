# Python-Looping-Calculator
A program that only uses "+" arithmetic operation to perform different functions such as finding sum, product, exponential and modulo of two numbers


Write a program in Python which performs the calculations detailed below. However, you should only use the arithmetic operation of “+”. You should make use of loop constructs and functions. You should consider how the return value of functions can be used to improve the readability of your program as well as the modularity, reducing the amount of repeated code.

The program should first enter into a main menu, giving the user a choice of entering the number "1" , "2", "3", or “4” . Entering the character "q" should exit the program.

If at any point in the program, the user enters invalid input, then the program should allow the user to enter the input again, but exceptions (ie: try/except) should not be used.

If the user enters "1" at the main menu:

The user should be prompted to enter two numbers, and the summation (addition) of the two numbers will be printed to screen.

To calculate this value, you should create a function with the following signature where x and y can be integer or float type, that returns the answer: sum(x,y).

If the user enters "2" at the main menu:

The user should be prompted to enter two positive numbers x and y, and the product of the two numbers will be printed to screen. The product of two numbers can be expressed as repeated addition operations. For example, 5*4 = 20; this can be calculated in an alternative way as (5+5+5+5) = 20.

To calculate this value, you should create a function with the following signature where x is an int or float, and y is an int, returning the answer: prod(x,y).

If the user enters "3" at the main menu:

The user should be prompted to enter two positive numbers, x and y. The value xy  should then be printed to screen. The raising of x to the power of y, can be expressed as repeated multiplications. For example,53=125; this can be alternatively expressed as 5*5*5=125.

To calculate this value, you should create a function with the following signature where x Is an integer, and y is an integer, that returns the answer : exp(x,y).

If the user enters “4” at the main menu:

The user should be prompted to enter two positive numbers, x and y. The value  should then be printed to screen. The modulo of x and y gives the remainder after ⌊xy⌋ ,  and can be expressed as repeated subtractions. For example, 5 mod 2 = 1; this can be alternatively expressed as 5-2-2=1.

To calculate this value, you should create a function with the following signature where x and y are both numbers, that returns the answer: modulo(x,y).

 

In your program you should:

Use variable and function names which consistently follow convention 
Use sensible design techniques, in order to make your program modular, readable and easy to maintain
Use comments to explain the functions and to explain your code
Follow the specified function names and signatures
Your program source file should contain a comment at the top with your full name 




You should not use any libraries, and a penalty will be imposed if libraries are used.

