from methodsProbability import *

print("Proability Methods")

selection = int(input("Enter the method to call: "))


prob = Probabilty(.50, .30, 5, 30)

print(prob.chance(5, 30))
print(prob.independent_events(.50, .30))

