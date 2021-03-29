from calculateStats import Statistics

f = open("stats.txt", "r")
statsStr = f.read()
statsList = list(statsStr.split("\n"))
del statsList[-1]

stats = Statistics(statsList)

print(stats.average())
print(stats.standardDeviation())
