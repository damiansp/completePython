from math import gamma

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def beta_pdf(x, a, b):
    return x**(a - 1) * (1 - x)**(b - 1) * gamma(a + b) / (gamma(a) * gamma(b))


class UpdateDistribution:
    def __init__(self, ax, prob=0.5):
        self.success = 0
        self.prob = prob
        self.line, = ax.plot([], [], 'k-')
        self.x = np.linspace(0, 1, 200)
        self.ax = ax

        # plot params
        self.ax.set_xlim(0, 1)
        self.ax.set_ylim(0, 15)
        self.ax.grid(True)

        # Theoretical value (plotted distrib. should converge to this)
        self.ax.axvline(prob, linestyle='--', color='k')

    def init(self):
        self.sucess = 0
        self.line.set_data([], [])
        return self.line,

    def __call__(self, i):
        if i == 0:
            return self.init()
        if np.random.rand(1,) < self.prob:
            self.success += 1
        y = beta_pdf(self.x, self.success + 1, (i - self.success) + 1)
        self.line.set_data(self.x, y)
        return self.line,


fig, ax = plt.subplots()
ud = UpdateDistribution(ax, prob=0.7)
anim = FuncAnimation(
    fig, ud, frames=np.arange(100), init_func=ud.init, interval=100, blit=True)
plt.show()
