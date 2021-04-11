from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt



class threeDGraph:
    def __init__(self, ax, fig):
        self.ax = ax
        self.fig = fig

    def f(self, x, y):
        return np.sin(np.sqrt(x ** 2 + y ** 2))

    def scatter_Graph(self):
        z = np.linspace(0, 1, 100)
        x = z * np.sin(25 * z)
        y = z * np.cos(25 * z)
        c = x + y
        self.ax.scatter(x, y, z, c=c)
        self.ax.set_title("3D Scatter Plot")
        plt.show()

    def contour(self):
        x = np.linspace(-6, 6, 30)
        y = np.linspace(-6, 6, 30)

        X, Y = np.meshgrid(x, y)
        Z = self.f(X, Y)
        fig = plt.figure()
        ax = plt.axes(projection='3d')
        ax.contour3D(X, Y, Z, 50, cmap='binary')
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_zlabel('z')
        ax.set_title('Contour')
        plt.show()

    def wireframe(self):
        x = np.linspace(-10, 10, 50)
        y = np.linspace(-10, 10, 50)
        X, Y = np.meshgrid(x, y)
        Z = self.f(X, Y)
        fig = plt.figure()
        ax = plt.axes(projection='3d')
        ax.plot_wireframe(X, Y, Z, color='blue')
        ax.set_title('Wireframe')
        plt.show()

    def surface_plot(self):
        x = np.linspace(-5, 5, 20)
        y = np.linspace(-5, 5, 20)

        X, Y = np.meshgrid(x, y)
        Z = self.f(X, Y)

        fig = plt.figure()
        ax = plt.axes(projection='3d')
        ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='viridis', edgecolor='none')
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_zlabel('z')
        ax.set_title('Surface Plot')
        plt.show()

    def surface_triangulations(self):
        x = np.linspace(-5, 5, 20)
        y = np.linspace(-5, 5, 20)

        X, Y = np.meshgrid(x, y)
        Z = self.f(X, Y)

        theta = 2 * np.pi * np.random.random(1000)
        r = 6 * np.random.random(1000)
        x = np.ravel(r * np.sin(theta))
        y = np.ravel(r * np.cos(theta))
        z = self.f(x, y)

        ax = plt.axes(projection='3d')
        ax.plot_trisurf(x, y, z, cmap='viridis', edgecolor='none')

        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_zlabel('z')
        ax.set_title('Surface Triangulations')

        plt.show()

    def mobius(self):
        x = np.linspace(-5, 5, 20)
        y = np.linspace(-5, 5, 20)

        X, Y = np.meshgrid(x, y)
        Z = self.f(X, Y)

        theta = np.linspace(0, 2 * np.pi, 30)
        w = np.linspace(-0.25, 0.25, 8)
        w, theta = np.meshgrid(w, theta)

        phi = 0.5 * theta

        # radius in x-y plane
        r = 1 + w * np.cos(phi)

        x = np.ravel(r * np.cos(theta))
        y = np.ravel(r * np.sin(theta))
        z = np.ravel(w * np.sin(phi))

        # triangulate in the underlying parametrization
        from matplotlib.tri import Triangulation
        tri = Triangulation(np.ravel(w), np.ravel(theta))

        ax = plt.axes(projection='3d')
        ax.plot_trisurf(x, y, z, triangles=tri.triangles,
                        cmap='viridis', linewidths=0.2);

        ax.set_xlim(-1, 1);
        ax.set_ylim(-1, 1);
        ax.set_zlim(-1, 1);

        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_zlabel('z')
        ax.set_title('Mobius Strip')

        plt.show()


#Source: jakevdp.github.io/PythonDataScienceHandbook/04.12-three-dimensional-plotting.html
