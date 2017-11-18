import matplotlib.pyplot as plt
import numpy as np


def plotbar(x, y):
    l = np.arange(len(x))
    plt.bar(l, x, align='center')
    plt.xticks(l, y)
    plt.show()