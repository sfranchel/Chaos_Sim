from chaos.ball import Ball
from chaos.support import Support
from chaos.simulator import Simulator
import matplotlib.pyplot as plt
import numpy as np

ball = Ball(10,0)
support = Support(A=3, f=0.5, z0=1)

dt = 0.00001

simulator = Simulator(support=support, ball=ball)

simulator.run_simulation(dt=dt, tmax=100, timeWindow=10)
df = simulator.get_history()

plt.plot(np.arange(len(df["ball_pos"]))*dt, df["ball_pos"])
plt.plot(df["time"], df["support_pos"])
plt.show()
