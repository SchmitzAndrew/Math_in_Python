def arithmeticN():
    a = int(input("What is the initial value? "))
    d = int(input("What is the difference between each value? "))
    n = int(input("What is the number you are finding? "))

    return a + d * (n - 1)


def arithmeticSum():
    a = int(input("What is the initial value? "))
    d = int(input("What is the difference between each value? "))
    n = int(input("What is the number of terms? "))

    return (n / 2) * (2 * a + d * (n - 1))


def geometricN():
    a = int(input("What is the initial value? "))
    r = int(input("What is the common ratio? "))
    n = int(input("What is the number you are finding? "))

    return a * (r ** (n - 1))


def geometricSum():
    #prevents value error with r
    a = float(input("What is the initial value? "))
    r = float(input("What is the common ratio? "))
    if r < -1 or r > 1:
        return "Invalid entry"
    n = float(input("What is the number of terms? "))

    fraction = (1 - (r ** n)) / (1 - r)

    return a * fraction
