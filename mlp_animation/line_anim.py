import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np
#from matplotlib.animation import FFMpegWriter


fig, ax = plt.subplots()
x = np.arange(0, 2 * np.pi, 0.01)
line, = ax.plot(x, np.sin(x))


def init(): # only required for blitting
    line.set_ydata([np.nan] * len(x))
    return line,


def animate(i):
    line.set_ydata(np.sin(x + i / 100)) # update data
    return line,


ani = animation.FuncAnimation(
    fig, animate, init_func=init, interval=2, blit=True, save_count=50)


plt.show()

# TO SAVE:
#ani.save('./movie.mp4')

# or
# writer = FFMpegWriter(fps=15, metadata=dict(artist='Me'), bitrate=1800)
# ani.save("movie.mp4", writer=writer)
