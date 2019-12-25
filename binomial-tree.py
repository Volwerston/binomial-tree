from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np 
import math 

S = 100
K = 100
r = 0.025
u = 1.05
d = 1/u
n = 32
T = 100

Rinv = math.exp(-r)
uu = u*u
p_up = (math.exp(r) - d)/(u - d)
p_down = 1 - p_up

prices = np.zeros(n+1)
prices[0] = S*math.pow(d, n)

for i in range(1, n+1):
    prices[i] = uu*prices[i-1]

call_values = np.zeros((n+1, n+1))
for i in range(0, n+1):
    call_values[n][i] = max(0.0, (prices[i] - K))

for step in range(n-1, -1, -1):
    for i in range(0, step+1):
        call_values[step][i] = (p_up*call_values[step+1][i+1] + p_down*call_values[step+1][i])*Rinv

print(call_values[0][0])

t = []
S = []
V = []

for i in range(0, n+1):
    for j in range(0, i+1):
        t += [i*(T/n)]
        S += [prices[j]]
        V += [call_values[i][j]]

fig = plt.figure()
ax = Axes3D(fig)

ax.scatter(t, S, V, s=1)

ax.set_xlabel('t')
ax.set_ylabel('S')
ax.set_zlabel('V')

plt.show()