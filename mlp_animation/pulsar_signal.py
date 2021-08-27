import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(8, 8), facecolor='black')
ax = plt.subplot(111, frameon=False)
ax.set_ylim(-1, 70)
ax.set_xticks([])
ax.set_yticks([])
ax.text(0.5,
        1.0,
        "MATPLOTLIB ",
        transform=ax.transAxes,
        ha="right",
        va="bottom",
        color="w",
        family="sans-serif",
        fontweight="light",
        fontsize=16)
ax.text(0.5,
        1.0,
        "UNCHAINED",
        transform=ax.transAxes,
        ha="left",
        va="bottom",
        color="w",
        family="sans-serif",
        fontweight="bold",
        fontsize=16)

# Random data
data = np.random.uniform(0, 1, (64, 75))
X = np.linspace(-1, 1, data.shape[-1])
G = 1.5 * np.exp(-4 * X**2)

# Gen line plots
lines = []
for i in range(len(data)):
    # Small reduction of the X extents to get a cheap perspective effect
    xscale = 1 - i/200.
    # Same for linewidth (thicker strokes on bottom)
    lw = 1.5 - i/100.0
    line, = ax.plot(xscale * X, i + G * data[i], color="w", lw=lw)
    lines.append(line)

    
def update(*args):
    # Shift all data to the right
    data[:, 1:] = data[:, :-1]

    # Fill in new values
    data[:, 0] = np.random.uniform(0, 1, len(data))

    # Update data
    for i in range(len(data)):
        lines[i].set_ydata(i + G*data[i])
    return lines

anim = animation.FuncAnimation(fig, update, interval=10)
plt.show()
