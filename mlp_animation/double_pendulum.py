import matplotlib.animation as anim
import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as integrate
from numpy import sin, cos


G = 9.8 # earth's gravity
L1 = 1. # length of pendulum 1
L2 = 2. # ''     '' ''       2
M1 = 1. # mass   '' ''       1
M2 = 10. # ''     '' ''       2
THETA1 = 120. # degrees
W1 = 0.       # angular velocity
THETA2 = -10.
W2 = 0.

def derivs(state, t):
    dydx = np.zeros_like(state)
    dydx[0] = state[1]
    del_ = state[2] - state[0]
    den1 = L1*(M1 + M2) - M2*L1*cos(del_)*cos(del_)
    dydx[1] = (M2*L1*state[1]*state[1]*sin(del_)*cos(del_)
               + M2*G*sin(state[2])*cos(del_)
               + M2*L2*state[3]*state[3]*sin(del_)
               - (M1 + M2)*G*sin(state[0])) / den1
    dydx[2] = state[3]
    den2 = den1*(L2 / L1)
    dydx[3] = (-M2*L2*state[3]*state[3]*sin(del_)*cos(del_)
               + (M1 + M2)*G*sin(state[0])*cos(del_)
               - (M1 + M2)*L1*state[1]*state[1]*sin(del_)
               - (M1 + M2)*G*sin(state[2])) / den2
    return dydx

# Create time array from 0... 100 at 0.05s steps
dt = 0.05
t = np.arange(0., 20, dt)

state = np.radians([THETA1, W1, THETA2, W2])
y = integrate.odeint(derivs, state, t)
x1 = L1*sin(y[:, 0])
y1 = -L1*cos(y[:, 0])
x2 = L2*sin(y[:, 2]) + x1
y2 = -L2*cos(y[:, 2]) + y1

fig = plt.figure()
ax = fig.add_subplot(
    111, autoscale_on=False, xlim=(-L1 - L2, L1 + L2), ylim=(-L1 - L2, L1 + L2))
ax.set_aspect('equal')
ax.grid()

line, = ax.plot([], [], 'o-', lw=2)
time_template = 'time: %.1fs'
time_text = ax.text(0.05, 0.9, '', transform=ax.transAxes)


def init():
    line.set_data([], [])
    time_text.set_text('')
    return line, time_text


def animate(i):
    thisx = [0, x1[i], x2[i]]
    thisy = [0, y1[i], y2[i]]
    line.set_data(thisx, thisy)
    time_text.set_text(time_template % (i*dt))
    return line, time_text

ani = anim.FuncAnimation(
    fig, animate, np.arange(1, len(y)), interval=25, blit=True, init_func=init)
plt.show()
