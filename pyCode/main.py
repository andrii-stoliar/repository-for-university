import matplotlib.pyplot as plt
import numpy as np
import math


l = 0.2
r = 0.05

#zadanie 1

t = np.arange(0, 25.1, 0.1)
rLK = [1, 0, -0.01, 0, 2]
rPK = [1, 0, 0.01, 0, 2]

counter = 0
alpha = 0
w = 0
V = 0

x = []
y = []

xl = []
yl = []
xp = []
yp = []

xo = 0
yo = 0

dx = 0
dy = 0

for i in range(251):
    if t[i] < 5:
        counter = 0
    elif t[i] < 10:
        counter = 1
    elif t[i] < 15:
        counter = 2
    elif t[i] < 20:
        counter = 3
    else:
        counter = 4
    VL = rLK[counter]
    VP = rPK[counter]
    V = (VP + VL) / 2
    w = (VP - VL) / l
    alpha = (w * 0.1) + alpha
    dx = (V * math.cos(alpha)) * 0.1
    dy = (V * math.sin(alpha)) * 0.1
    x.append(xo + dx)
    y.append(yo + dy)

    xl.append(x[i] - math.sin(alpha)*l)
    yl.append(y[i] + math.cos(alpha)*l)
    xp.append(x[i] + math.sin(alpha)*l)
    yp.append(y[i] - math.cos(alpha)*l)

    xo = x[i]
    yo = y[i]

plt.plot(x, y, color='black', label='Robot')
plt.plot(xl, yl, color='green', label='Lave Koleso')
plt.plot(xp, yp, color='red', label='Prave Koleso')
plt.xlabel('x')
plt.ylabel('y')
plt.title('1 zadanie')
plt.legend()
plt.show()

#zadanie 2

#----------
# ukazte dlzku stvorca v [sm] (def.15[sm])
ls = 2
#----------

t2 = np.arange(0, 45.1, 0.1)
rLK = [ls/5, -0.01*math.pi, ls/5, -0.01*math.pi, ls/5, -0.01*math.pi, ls/5, -0.01*math.pi, ls/10]
rPK = [ls/5, 0.01*math.pi, ls/5, 0.01*math.pi, ls/5, 0.01*math.pi, ls/5, 0.01*math.pi, ls/10]

counter = 0
alpha = 0
w = 0
V = 0

x = []
y = []

xl = []
yl = []
xp = []
yp = []

xo = 0
yo = 0

dx = 0
dy = 0

for j in range(len(t2)):
    if t2[j] < 5:
        counter = 0
    elif t2[j] < 10:
        counter = 1
    elif t2[j] < 15:
        counter = 2
    elif t2[j] < 20:
        counter = 3
    elif t2[j] < 25:
        counter = 4
    elif t2[j] < 30:
        counter = 5
    elif t2[j] < 35:
        counter = 6
    elif t2[j] < 40:
        counter = 7
    else:
        counter = 8
    VL = rLK[counter]
    VP = rPK[counter]
    V = (VP + VL) / 2
    w = (VP - VL) / l
    alpha = (w * 0.1) + alpha
    dx = (V * math.cos(alpha)) * 0.1
    dy = (V * math.sin(alpha)) * 0.1
    x.append(xo + dx)
    y.append(yo + dy)

    xl.append(x[j] - math.sin(alpha)*l)
    yl.append(y[j] + math.cos(alpha)*l)
    xp.append(x[j] + math.sin(alpha)*l)
    yp.append(y[j] - math.cos(alpha)*l)

    xo = x[j]
    yo = y[j]

plt.plot(x, y, color='black', label='Robot')
plt.plot(xl, yl, color='green', label='Lave Koleso')
plt.plot(xp, yp, color='red', label='Prave Koleso')
plt.xlabel('x')
plt.ylabel('y')
plt.title('2 zadanie')
plt.legend()
plt.show()

#3 zadanie

#----------
# ukazte R1 R2 a L v [sm] (def.15[sm])
R1 = 15
R2 = 15
L = 15
#----------

rLK3 = [-0.01*math.pi, ((math.pi*R1)/5)/(((10*R1 - 1)/(10*R1 + 1))+1), L/5, ((math.pi*R2)/5)/(((10*R2 + 1)/(10*R2 - 1))+1)]
rPK3 = [0.01*math.pi, ((math.pi*R1)/5)/(((10*R1 + 1)/(10*R1 - 1))+1), L/5, ((math.pi*R2)/5)/(((10*R2 - 1)/(10*R2 + 1))+1)]

t3 = np.arange(0, 20.1, 0.1)

counter = 0
alpha = 0
w = 0
V = 0

x3 = []
y3 = []

xl3 = []
yl3 = []
xp3 = []
yp3 = []

xo = 0
yo = 0

dx = 0
dy = 0

for k in range(len(t3)):
    if t3[k] < 5:
        counter = 0
    elif t3[k] < 10:
        counter = 1
    elif t3[k] < 15:
        counter = 2
    else:
        counter = 3
    VL = rLK3[counter]
    VP = rPK3[counter]
    V = (VP + VL) / 2
    w = (VP - VL) / l
    alpha = (w * 0.1) + alpha
    dx = (V * math.cos(alpha)) * 0.1
    dy = (V * math.sin(alpha)) * 0.1
    x3.append(xo + dx)
    y3.append(yo + dy)

    xl3.append(x3[k] - math.sin(alpha)*l)
    yl3.append(y3[k] + math.cos(alpha)*l)
    xp3.append(x3[k] + math.sin(alpha)*l)
    yp3.append(y3[k] - math.cos(alpha)*l)

    xo = x3[k]
    yo = y3[k]

plt.plot(x3, y3, color='black', label='Robot')
plt.plot(xl3, yl3, color='green', label='Lave Koleso')
plt.plot(xp3, yp3, color='red', label='Prave Koleso')
plt.xlabel('x')
plt.ylabel('y')
plt.title('3 zadanie')
plt.legend()
plt.show()







