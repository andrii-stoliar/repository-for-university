import keyboard  # pip install keyboard
import math
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

l = 0.2
V = 0.1
w = 0

dx = 0
dy = 0


alpha = 0
xo = 0
yo = 0

x = [xo]
y = [yo]

xl = []
yl = []
xp = []
yp = []

t = range(10000)
def update_V_inc():
    global V
    V += 0.1

def update_V_dec():
    global V
    V -= 0.1

def update_w_inc():
    global w
    w += 0.1

def update_w_dec():
    global w
    w -= 0.1

def stop_V():
    global V
    V = 0

def stop_w():
    global w
    w = 0

def stop():
    global w
    global V
    V = 0
    w = 0

# bind the buttons to the functions
keyboard.add_hotkey('up', update_V_inc)
keyboard.add_hotkey('down', update_V_dec)
keyboard.add_hotkey('right', update_w_dec)
keyboard.add_hotkey('left', update_w_inc)
keyboard.add_hotkey('v', stop_V)
keyboard.add_hotkey('b', stop_w)
keyboard.add_hotkey('space', stop)

fig, ax = plt.subplots()
def update(frame):
    global dx, dy, alpha, xo, yo, x, y, xl, yl, xp, yp, V, w

    if frame == 0:
        return ax.plot([], [])

    alpha = (w * 0.1) + alpha
    dx = (V * math.cos(alpha)) * 0.1
    dy = (V * math.sin(alpha)) * 0.1
    x.append(xo + dx)
    y.append(yo + dy)

    xl.append(x[frame] - math.sin(alpha) * l)
    yl.append(y[frame] + math.cos(alpha) * l)
    xp.append(x[frame] + math.sin(alpha) * l)
    yp.append(y[frame] - math.cos(alpha) * l)

    xo = x[frame]
    yo = y[frame]

    ax.clear()
    ax.plot(x, y, 'black')
    ax.plot(xl, yl, 'g')
    ax.plot(xp, yp, 'r')
    xlim = [-15, 15]
    ylim = [-15, 15]
    ax.set_xlim(xlim)
    ax.set_ylim(ylim)
    ax.set_aspect('equal')

    return ax.plot(x, y, 'black')

ani = FuncAnimation(fig, update, frames=range(10000), interval=100)

plt.show(block=True)



