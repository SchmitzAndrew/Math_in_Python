from methodsSeries import *

print("Series Methods")
print("1 - Arithmetic- Find Nth Term")
print("2- Arithmetic- Find Sum")
print("3- Geometric- Find Nth Term")
print("4- Geometric- Find Sum")

input = int(input("Enter the method to call: "))

if input == 1:
	print(arithmeticN())
elif input == 2:
	print(arithmeticSum())
elif input == 3:
	print(geometricN())
elif input == 4:
	print(geometricSum())
else:
	print("Invalid Selection")
