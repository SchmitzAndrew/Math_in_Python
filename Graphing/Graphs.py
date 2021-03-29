import matplotlib.pyplot as plt


# graph modulus
def modulus():
    mod_x_axis = [*range(-10, 10, 1)]
    mod = 5
    mod_y_axis = [y % mod for y in range(-10, 10, 1)]

    plt.plot(mod_x_axis, mod_y_axis)
    plt.show()


# graph polynomial
def polynomial():
    degree = float(input("What degree polynomial? "))
    poly_x_axis = [*range(-10, 10, 1)]
    poly_y_axis = [y ** degree for y in range(-10, 10, 1)]

    plt.plot(poly_x_axis, poly_y_axis)
    plt.show()


# choose:
choice = int(input("Which graph? "))
if choice == 1:
    modulus()
elif choice == 2:
    polynomial()
