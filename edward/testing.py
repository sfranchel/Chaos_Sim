from chaos.ball import Ball
from chaos.support import Support
from chaos.simulator import Simulator

import matplotlib.pyplot as plt
import numpy as np

ball = Ball(10, 0)

# support = Support(A= 10, f= 100, z0 = )
# system = System(support, [ball, ball2, ball3])

def plat_mov(tmax, A,f,z0):
    t = np.arange(0,tmax, dt)
    x = A* np.sin(2*np.pi * f * t) + z0 
    return t,x

def sliced_plat_pos(x_plat,i,j):
    return x_plat[i:j]

def ball_mov(time_window, x0, v0):
    t = np.arange(0, time_window , dt)
    x = -1./2 * 9.81*t**2 + v0*t + x0
    return t, x

dt = 0.001
t_max = 100
time_window = 5 # sec
nb_indices_window = int(time_window/dt)
positions = []

ti = 0 
i = 0
x0 = 10
v0 = 10
t_plat,x_plat = plat_mov(tmax=t_max, A=3, f=0.5, z0= 1)
while ti < t_max :
    print("")
    t_ball,x_ball = ball_mov(time_window=time_window, x0=x0, v0=v0) 
    sl_plat = sliced_plat_pos(x_plat,i,i+nb_indices_window)
    if len(x_ball) != len(sl_plat):
        print("No more intersection")
        break
    bb = (x_ball <= sl_plat).argmax() - 1
    if bb == -1 :
        print("No intersections ! ")
        break
    hist_x_ball = x_ball[:bb]
    positions.append(hist_x_ball)
    ti = (i+bb) * dt
    # x_ball_bb = x_ball[bb] # = x0
    x0 = x_ball[bb]
    i = i+bb
    print(ti)


hist_pos = np.array([])
for i in positions:
    hist_pos = np.append(hist_pos,i)

t_all = np.arange(len(hist_pos)) * dt
    
plt.plot(t_all, hist_pos)
plt.plot(t_plat, x_plat)
plt.show()











# plt.plot(t,x_plat)
# plt.show()



# plt.plot(system.balls_history_posX[0])
# plt.plot(system.balls_history_posX[1])
# plt.plot(system.balls_history_posX[2])
# plt.show()
    
