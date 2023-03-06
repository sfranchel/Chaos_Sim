from .ball import Ball
from .support import Support
import numpy as np
from numba import jit  # import the types


class Simulator:
    def __init__(self, support: Support, ball: Ball) -> None:
        self.ball = ball
        self.support = support

        self.support_history_posX: list = []
        self.__history = {
            "time": [],
            "ball_pos": [],
            "supp_pos": [],
        }
        self.t = 0

    @jit()
    def run_simulation(self, tmax: float, dt: float):
        while self.t < tmax:
            self.support.update(self.t)
            self.ball.update(dt)
            self.check_impact()

            self.__history["ball_pos"].append(self.ball.x)
            self.__history["supp_pos"].append(self.support.x)
            self.t += dt


    def check_impact(self):
        # if self.ball.x < self.support.x:
        if self.ball.x < self.support.x:
            self.ball.x = self.support.x
            self.ball.v = self.support.absorbance * (-self.ball.v + self.support.v) - self.support.v

    def get_history(self):
        return self.__history
