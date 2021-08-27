import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D


class Scope:
    def __init__(self, ax, max_t=2, dt=0.02):
        self.ax = ax
        self.dt = dt
        self.max_t = max_t
        self.t_data = [0]
        self.y_data = [0]
        self.line = Line2D(self.t_data, self.y_data)
        self.ax.add_line(self.line)
        self.ax.set_ylim(-0.1, 1.1)
        self.ax.set_xlim(0, self.max_t)

    def update(self, y):
        last_t = self.t_data[-1]
        if last_t > self.t_data[0] + self.max_t:  # reset the arrays
            self.t_data = [self.t_data[-1]]
            self.y_data = [self.y_data[-1]]
            self.ax.set_xlim(self.t_data[0], self.t_data[0] + self.max_t)
            self.ax.figure.canvas.draw()

        t = self.t_data[-1] + self.dt
        self.t_data.append(t)
        self.y_data.append(y)
        self.line.set_data(self.t_data, self.y_data)
        return self.line,


def emitter(p=0.03):
    '''return a random value with probability p, else 0'''
    while True:
        v = np.random.rand(1)
        if v > p:
            yield 0.
        else:
            yield np.random.rand(1)


fig, ax = plt.subplots()
scope = Scope(ax)

# pass a generator in "emitter" to produce data for the update func
ani = animation.FuncAnimation(
    fig, scope.update, emitter, interval=10, blit=True)
plt.show()
