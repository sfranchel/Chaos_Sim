# import scipy.constants as cst
import numpy as np


class Ball:
    def __init__(self, y0, v0) -> None:
        """
        Constructor for Ball class
        - y0 : initial position (cm)
        - v0 : initial velocity (cm)
        """
        self.posY0 = y0
        self.velY0 = v0

        self.posY: np.ndarray
        self.velY : np.ndarray

    def compute_positions(self, timeWindow: float, dt: float) -> None:
        t = np.arange(0,timeWindow, dt)
        self.posY = -1.0 / 2 * 9.81 * t**2 + self.velY0 * t + self.posY0
        self.velY = -9.81 * t + self.velY0
        

        # compute kinematics instead
        

    # def get_positions():
