
import matplotlib.pyplot as plt
def graph(pi, numbers):
    # x axis values
    x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    # corresponding y axis values
    y = numbers

    #bar labels
    tick_label = [str(t) for t in x]

    plt.bar(x, y, tick_label = tick_label)

    # naming the x axis
    plt.xlabel('x - axis')
    # naming the y axis
    plt.ylabel('y - axis')

    plt.title('Graphs the frequency of the digits of pi.')

    # function to show the plot
    plt.show()


