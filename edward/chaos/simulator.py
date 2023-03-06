from .ball import Ball
from .support import Support
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



class Simulator:
    def __init__(self, support: Support, ball: Ball) -> None:
        self.ball = ball
        self.support = support

        self.currentImpactTime = 0
        self.currentImpactIndex = 0

        self.__history = {"time": [], "support_pos": [], "ball_pos": [], "t_impact": []}
        
        self.t = np.ndarray

        # self.balls_history_velX : list[list] = [[] for _ in range(len(balls))]

    def check_collision(self, i, j):
        """
        Finds the collison index between the ball and the support during the interval i<->j

        Parameters:
        ---
        i : lower bound index
        j : upper bound index

        Returns:
        ---
        ci : collision index
        """

        sliced_pos = self.support.get_sliced_positions(i, j)
        # print(sliced_pos)
        if len(self.ball.posY) != len(sliced_pos):
            return -2
        ci = (self.ball.posY <= sliced_pos).argmax() - 1
        return ci

    def run_simulation(self, dt: float, tmax: float, timeWindow: float, progressBarObj=None):
        """
        Starts the simulation.

        Parameters
        ---
        dt : increment of time for th simulation
        tmax : the time which the simulation will stop
        timeWindow : width of the window where to look for the intersection with the support
        """
        
        self.t = np.arange(0, tmax, dt)
        indicesTimeWindow = int(timeWindow / dt)

        # calcul toutes les positions du support
        self.support.compute_positions(self.t)
        while self.currentImpactTime < tmax:
            self.ball.compute_positions(timeWindow, dt)
            bb = self.check_collision(
                self.currentImpactIndex, self.currentImpactIndex + indicesTimeWindow
            )

            if bb == -2:
                # print("No more intersections, end of simulation")
                # self.currentImpactTime = tmax
                break
            elif bb == -1:
                # print("No intersections ! Check the time window ")
                break
            elif bb == 0:
                # print("Stick the support ?")
                break

            self.currentImpactTime = (self.currentImpactIndex + bb) * dt
            self.currentImpactIndex += bb

            self.__update_ball_kinematics(bb)
            self.__history["ball_pos"] += self.ball.posY[:bb].tolist()
            self.__history["t_impact"].append(self.currentImpactTime)
            
            # yield self.currentImpactTime/ tmax * 100

        self.__history["time"] = self.t.tolist()
        self.__history["support_pos"] = self.support.pos_vals.tolist()

    def get_history(self):
        return self.__history

    def __update_ball_kinematics(self, localBallIndex):
        """
        Computes the new positions and speed given the ball's impact index.
        """
        self.ball.posY0 = self.ball.posY[localBallIndex]
        self.ball.velY0 = 1.0 * (
            -self.ball.velY[localBallIndex] + self.support.velX[self.currentImpactIndex]
        )
