import matplotlib.pyplot as plt

e = 2.71828
pi = 3.1415

def graphNormal(mean, standard_deviation):
    normal_x_axis = [i/10 for i in range(-50, 50)] #range doesnt allow floats as steppers
    normal_y_axis = []
    for x in normal_x_axis:
        frac = (1 / (standard_deviation * ((2 * pi) ** .5)))
        exponent = (e ** (-.5 * ((x - mean) / standard_deviation) ** 2))
        f = frac * exponent
        normal_y_axis.append(f)
    plt.plot(normal_x_axis, normal_y_axis)
    plt.show()

graphNormal(float(input("Enter the mean: ")), float(input("Enter the SD: ")))


