class Ball:
    '''
    Class for a free falling ball
    '''

    # Gravitational acceleration
    g=9.80665  # m/s^2

    # Constructor method
    def __init__(self, x0=0, v0=0):
            self.pos = x0   # m
            self.vel = v0   # m/s
            self.pos0 = x0
            self.vel0 = v0
            self.t = 0

    # Reset Method, to be used after collisions
    def reset(self, x0,v0): 
        self.pos = x0
        self.vel = v0
        self.pos0 = x0
        self.vel0 = v0
        self.t = 0

    # Evolve in time according to parablic motion
    def evolve(self,dt):
        self.t += dt
        self.pos = self.pos0 + self.vel0*self.t - 0.5*Ball.g*self.t**2
        self.vel = self.vel0 - Ball.g*self.t