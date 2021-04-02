from methodsRecursion import *

print("Recursive Methods")

selection = int(input("Enter the method to call: "))

if selection == 1:
    numbers = int(input("Enter the numbers to generate: "))
    for n in range(numbers):
        print(fibonacci(n))

elif selection == 2 :
    number = int(input("Enter the number to find the factorial of: "))
    factorial(number)

else:
    print("Not a valid selection")



