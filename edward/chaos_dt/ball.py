import scipy.constants as cst
from numba import int32, float32    # import the types
from numba.experimental import jitclass

# @jitclass()
class Ball:
    def __init__(self, y0: float, v0: float) -> None:
        """
        Constructor for Ball class
        - y0 : initial position (cm)
        - v0 : initial velocity (cm)
        """
        self.x = y0
        self.v = v0
        self.x0 = y0
        self.v0 = v0
        self.tImpact = 0

        self.previousX = 0
        self.previousV = 0

    def update(self, t: float) -> None:
        """
        Evolution of the ball for a specific time
        - dt : increment of time
        """
        
        self.v += -9.81 * t
        self.x += self.v*t

        self.previousX = self.x
        self.previousV = self.v
