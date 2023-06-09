import matplotlib.pyplot as plt
import numpy as np
import random

font1 = {"family": "serif", "color": "blue", "size": 20}
font2 = {"family": "serif", "color": "darkred", "size": 15}
fonts = list((font1, font2))


def graph1(pos):
    plt.subplot(2, 2, pos)
    plt.title("Graph", fonts.copy().pop(random.randint(0, 1)))
    xpoints = np.array([0, 6])
    ypoints = np.array([0, 250])
    plt.plot(xpoints, ypoints)


def graph2(pos):
    plt.subplot(2, 2, pos)
    plt.title("Graph", fonts.copy().pop(random.randint(0, 1)))
    ypoints = np.array([2, 100, 23, 66])
    plt.plot(ypoints, ".:")


def scatter(pos):
    plt.subplot(2, 2, pos)

    x = np.array([5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6])
    y = np.array([99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86])
    colors = np.array([0, 10, 20, 30, 40, 45, 50, 55, 60, 70, 80, 90, 100])
    
    plt.scatter(x, y, c=colors, cmap="viridis")
    plt.colorbar()

def randomScatter(num, size):
    x = np.random.randint(num, size=num)
    y = np.random.randint(num, size=num)
    colours = np.random.randint(num, size=num)
    sizes = 10 * np.random.randint(size, size=num)
    plt.scatter(x, y, s=sizes, c=colours, alpha=0.5, cmap="nipy_spectral")
    plt.colorbar()


randomScatter(100, 100)
plt.show()
