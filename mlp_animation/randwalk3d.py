import matplotlib.animation as animation
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
import numpy as np


def gen_rand_line(length, dims=2):
    line_data = np.empty([dims, length])
    line_data[:, 0] = np.random.rand(dims)
    for index in range(1, length):
        step = (np.random.rand(dims) - 0.5) * 0.1
        line_data[:, index] = line_data[:, index - 1] + step
    return line_data


def update_lines(n, data_lines, lines):
    for line, data in zip(lines, data_lines):
        line.set_data(data[0:2, :n])
        line.set_3d_properties(data[2, :n])
    return lines


N_LINES = 3
LINE_LENGTH = 500
DIMS = 3

fig = plt.figure()
ax = p3.Axes3D(fig)
data = [gen_rand_line(LINE_LENGTH, DIMS) for index in range(N_LINES)]
lines = [ax.plot(d[0, 0:1], d[1, 0:1], d[2, 0:1])[0] for d in data]

ax.set_xlim3d([0., 1.])
ax.set_ylim3d([0., 1.])
ax.set_zlim3d([0., 1.])
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('3D Test')
line_ani = animation.FuncAnimation(fig,
                                   update_lines,
                                   LINE_LENGTH,
                                   fargs=(data, lines),
                                   interval=N_LINES,
                                   blit=False)
plt.show()
