from Simulator.Ball import Ball
from Simulator.Platform import Platform
from Simulator.Solvers import *

from numpy import pi

class ChaoticSystem:
    def __init__(self, x0, v0, A0, w0, mu=1):
        self.ball = Ball(x0,v0)
        self.platform = Platform(A0, w0)
        self.mu = mu

        self.last_T = 0
        self.ball_is_stuck=False

        # Collections of output observables
        self.t_coll = []
        self.phi_coll = []
        self.I_coll = []

    # Get Methods
    def get_ball_x(self): return self.ball.pos
    def get_platform_x(self): return self.platform.pos

    # Set Methods
    def set_platform_A(self,A): self.platform.A = A
    def set_platform_w(self,w): self.platform.w = w

    def reset(self):
        self.t_coll=[]
        self.phi_coll=[]

    def evolve(self,dt):

        # retrieve the ball and the platform
        ball = self.ball
        platform = self.platform

        # evolve step
        ball.evolve(dt)
        platform.evolve(dt)

        # The ball might detach from the platfrom, when the latter is rising.
        if platform.vel > 0 and self.ball_is_stuck:
            self.ball_is_stuck=False

        # check if ball has interacted with platform
        if ball.pos <= platform.pos:
            if abs(ball.vel - platform.vel) > 0.01 and not self.ball_is_stuck: 
                self.collide(dt, ball, platform)
            else:
                self.ball_is_stuck=True
                ball.reset(platform.pos, platform.vel)
                self.last_T = (2*pi-platform.phi)/platform.w

    def collide(self, dt, b, p):
        # find best apporx for intersection point
        # knowing that in the last dt ball and plaform have interacted
        t_int = Bisection_solver( dt, b.pos, b.vel, p.A, p.w, p.phi)

        # evolve back to the interaction time, N.B. t_int is a negative time
        b.evolve(t_int)
        p.evolve(t_int)
        self.t_coll.append(b.t* (p.w/(2*pi))) # Time in units of Periods
        self.phi_coll.append((b.t -self.last_T)*p.w/(2*pi)) # Difference of Phase
        self.last_T = (2*pi - p.phi)/p.w

        # change ball direction
        v_in = b.vel
        b.reset(b.pos,-self.mu*(b.vel - p.vel) + p.vel)
        self.I_coll.append(v_in - b.vel)

        # finish evoloution
        b.evolve(-t_int)
        p.evolve(-t_int)
