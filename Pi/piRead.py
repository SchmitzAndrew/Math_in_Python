# Analyzes the digits of pi
from analyzePi import graph

f = open("pi.txt", "r")
pi = f.read()

# list that represents each digit
numbers = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

def split(n):
    if n == 0:
        numbers[0] += 1
    elif n == 1:
        numbers[1] += 1
    elif n == 2:
        numbers[2] += 1
    elif n == 3:
        numbers[3] += 1
    elif n == 4:
        numbers[4] += 1
    elif n == 5:
        numbers[5] += 1
    elif n == 6:
        numbers[6] += 1
    elif n == 7:
        numbers[7] += 1
    elif n == 8:
        numbers[8] += 1
    elif n == 9:
        numbers[9] += 1


for n in range(0, len(pi) - 1):
    try:
        split(int(pi[n]))
    except ValueError: #avoids error from newline chars
        pass

graph(pi, numbers)
