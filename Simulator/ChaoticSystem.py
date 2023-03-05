from Simulator.Ball import ball
from Simulator.Platform import platform
from Simulator.Solvers import *

class chaotic_system:
    def __init__(self, x0, v0, A0, w0, mu=1):
        self.__ball = ball(x0,v0)
        self.__platform = platform(A0, w0)
        self.__mu = mu
        self.__t_coll = []
        self.__last_T = 0
        self.__phi_coll = []
        self.__ball_is_stuck=False

    # Get Methods
    def get_t_collisions(self): return self.__t_coll
    def get_ball_x(self): return self.__ball.get_x()
    def get_platform_x(self): return self.__platform.get_x()

    # Set Methods
    def set_platform_A(self,A): self.__platform.set_A(A)
    def set_platform_w(self,w): self.__platform.set_w(w)
    def reset_ball(self,x0,v0): self.__ball.reset(x0,v0)
    def reset_platform(self,A=None,w=None): self.__platform.reset(A,w)
    def reset(self): self.__t_coll=[]

    def evolve(self,dt):

        # retrieve the ball and the platform
        _ball = self.__ball
        _platform = self.__platform

        # evolve step
        if _ball.get_x() <= _platform.get_x() and not self.__ball_is_stuck:
            print('warning something wrong!!!!')
            print(_ball)
            print(_platform)
        _ball.evolve(dt)
        _platform.evolve(dt)

        if _platform.get_v()>0 and self.__ball_is_stuck:
            self.__ball_is_stuck=False

        # check if ball has interacted with platform
        if _ball.get_x() <= _platform.get_x():
            if abs(_ball.get_v() - _platform.get_v()) > 0.01 and not self.__ball_is_stuck: 
                self.collide(dt, _ball, _platform)
            else:
                self.__ball_is_stuck=True
                _ball.reset(_platform.get_x(), _platform.get_v())

    def collide(self, dt, b, p):
        # Step back
        b.evolve(-dt)
        p.evolve(-dt)

        # Find time of interaction
        try:
            t_int = Newton_solver(dt, b.get_x0(), b.get_v0(), b.get_t(), p.get_A(), p.get_w(), p.get_phi())
        except:
            print('WARNING: Newton_solver failed, fallig back to Bisection_solver')
            t_int = Bisection_solver( dt, b.get_x(), b.get_v(), p.get_A(), p.get_w(), p.get_phi())

        # evolve to the interaction time
        b.evolve(t_int)
        p.evolve(t_int)
        self.__t_coll.append(b.get_t())

        # change ball direction ball
        b.reset(b.get_x(),-self.__mu*(b.get_v() - p.get_v()) + p.get_v())

        # finish evoloutuon
        b.evolve(dt-t_int)
        p.evolve(dt-t_int)
