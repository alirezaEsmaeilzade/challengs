import random
import matplotlib.pyplot as plt
from matplotlib import image
import numpy as np
from scipy.interpolate import BSpline


def cal(K, T, C):
    data = image.imread('static/Batman.jpg')
    k = int(K)
    t = list(range(0, int(T)))
    c = random.sample(range(-len(t) + 1, len(t) - 1), len(t) - 1)
    spl = BSpline(t, c, k)
    #fig, ax = plt.subplots()
    xx = np.linspace(0, C, 10)
    plt.plot(xx, spl(xx), 'b-', label='BSpline')
    plt.grid(True)
    plt.legend(loc='best')
    plt.axis('off')
    #plt.imshow(data)
    plt.show()
    #plt.savefig("static/plot.png")

cal(2, 8, 2)