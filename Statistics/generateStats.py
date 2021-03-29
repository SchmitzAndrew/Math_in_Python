import random

f = open("stats.txt", "w")

for i in range(1000):
    f.write(str(random.randint(1, 100)) + '\n')


f.close()
