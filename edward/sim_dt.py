from chaos_dt.ball import Ball
from chaos_dt.support import Support
from chaos_dt.simulator import Simulator
import matplotlib.pyplot as plt
from numba import int32, float32    # import the types
from numba.experimental import jitclass
import numba

support = Support(2, 0.2, 2, absorbance=1.)
ball = Ball(10, 3)
simulator = Simulator(support=support, ball=ball)
simulator.run_simulation(10, 0.001)
h = simulator.get_history()


plt.plot(h["ball_pos"], marker="")
plt.plot(h["supp_pos"])
plt.show()

print(numba.typeof(ball))
