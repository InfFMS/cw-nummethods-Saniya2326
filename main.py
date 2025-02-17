import numpy as np
import matplotlib.pyplot as plt

b = 3.19*10**-5
a = 0.1382




def P(v,t):
    y = (8.31*t)/(v-b)-(a/v**2)
    return y



x = np.linspace(b+10**-5,10**-3,100000)

y1 = []
y2 = []
y3 = []
y4 = []
y5 = []



for i in range(0, len(x)):
    t = -140 + 273.15
    p = P(x[i], t)
    y1.append(p)
    t = - 130 + 273.15
    p = P(x[i], t)
    y2.append(p)
    t = - 120 + 273.15
    p = P(x[i], t)
    y3.append(p)
    t = - 110 + 273.15
    p = P(x[i], t)
    y4.append(p)
    t = - 100 + 273.15
    p = P(x[i], t)
    y5.append(p)



fig, ax = plt.subplots(2, 3, figsize=(14,6))

ax[0][0].plot(x, y1)


ax[0][1].plot(x, y2)
ax[0][1].set_title("T = - 130℃")



ax[0][2].plot(x, y3)


ax[1][0].plot(x, y4, color='red')



ax[1][1].plot(x, y5)


fig, ax = plt.subplots(1, 1, figsize=(14,5))
plt.plot(x, y2)
plt.grid()

n = 5.23*10**-5

while P(n, -130+273.15)>P(n+0.0000001, 273.15-130):
    n = n+0.00000001

k = 10**-5*9.9
while P(k, -130+273.15)>P(k-0.0000001, 273.15-130):
    k = k-0.00000001

print('минимум',P(n,  273.15-130), 'максимум',P(k,  273.15-130))

plt.show()
