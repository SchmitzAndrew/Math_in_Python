import matplotlib.pyplot as plt

#module imports
from Graphs import *
from threeDimensionalGraphs import threeDGraph
from multiDimensionalGraphs import multiDScatterPlot

print("Graphing with matplotlib")

print("2D Graphs: ")
print("1 - Modulus")
print("2 - Polynomial")

print("Multi Dimensional Graphs: ")

print("3 - 3D Scattered Graph")
print("4 - Contour")
print("5 - Wireframe")
print("6 - Surface Plot ")
print("7 - Surface Triangulations")
print("8 - Mobius Strip")
print("9 - 4D Graph")



selection = int(input("Enter the method to call: "))

#creates object
ax = plt.axes(projection="3d")
fig = plt.figure()
graph3D = threeDGraph(ax, fig)

if selection == 1:
    modulus()
elif selection == 2:
    polynomial()
elif selection == 3:
    graph3D.scatter_Graph()
elif selection == 4:
    graph3D.contour()
elif selection == 5:
    graph3D.wireframe()
elif selection == 6:
    graph3D.surface_plot()
elif selection == 7:
    graph3D.surface_triangulations()
elif selection == 8:
    graph3D.mobius()
elif selection == 9:
    multiDScatterPlot()
else:
    print("Not a valid selection")






