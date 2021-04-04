from calculateStats import Statistics

from generateStats import generate_coordinates

#Reads txt of data points
f = open("statsNumbers.txt", "r")
statsStr = f.read()
statsList = list(statsStr.split("\n"))
del statsList[-1]


#Creates list of coordinates
coordinatesList = generate_coordinates(15, 15, 25)

#Creates Stats Object
stats = Statistics(statsList, coordinatesList)

print("1- Single Var Stats: ")
print("2 - Best Fit: ")

selection = int(input("Enter the method to call: "))

if selection == 1:
    print(stats.average())
    print(stats.standardDeviation())
    print(stats.sampleStandDardDeviation())
    print(stats.median())
    print(stats)
elif selection == 2:
    stats.bestFit()
else:
    print("Not a valid solution")
