import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation


fig = plt.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1], frameon=False)
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_xticks([])
ax.set_yticks([])

n_drops = 50
rain_drops = np.zeros(n_drops, dtype=[('position', float, 2),
                                      ('size', float, 1),
                                      ('growth', float, 1),
                                      ('color', float, 4)])
rain_drops['position'] = np.random.uniform(0, 1, (n_drops, 2))
rain_drops['growth'] = np.random.uniform(50, 200, n_drops)

scat = ax.scatter(rain_drops['position'][:, 0],
                  rain_drops['position'][:, 1],
                  s=rain_drops['size'],
                  lw=0.5,
                  edgecolors=rain_drops['color'],
                  facecolors='none')

def update(frame_number):
    current_idx = frame_number % n_drops

    # Make colors more transparent with time
    rain_drops['color'][:, 3] -= 1. / len(rain_drops)
    rain_drops['color'][:, 3] = np.clip(rain_drops['color'][:, 3], 0, 1)

    # Bigger circles with time
    rain_drops['size'] += rain_drops['growth']

    rain_drops['position'][current_idx] = np.random.uniform(0, 1, 2)
    rain_drops['size'][current_idx] = 5
    rain_drops['color'][current_idx] = (0, 0, 0, 1)
    rain_drops['growth'][current_idx] = np.random.uniform(50, 200)

    scat.set_edgecolors(rain_drops['color'])
    scat.set_sizes(rain_drops['size'])
    scat.set_offsets(rain_drops['position'])

    
animation = FuncAnimation(fig, update, interval=10)
plt.show()

                                      

