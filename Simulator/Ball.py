class ball:
    '''
    Class for a free falling ball
    '''

    # Gravitational acceleration
    __g=9.80665  # m/s^2

    # Constructor method
    def __init__(self, x0=0, v0=0):
            self.__px = x0   # m
            self.__vx = v0   # m/s
            self.__p0 = x0
            self.__v0 = v0
            self.__t = 0

    def __str__(self):
        __str  = f'Ball info:\n'
        __str += f'\tpx={self.__px:.7f}, vx={self.__vx:.7f}\n'
        __str += f'\tp0={self.__p0:.7f}, v0={self.__v0:.7f}, t={self.__t:.7f}' 
        return __str

    # Get methods
    def get_x(self): return self.__px
    def get_v(self): return self.__vx
    def get_x0(self): return self.__p0
    def get_v0(self): return self.__v0
    def get_t(self): return self.__t

    # Set methods
    def set_x(self, px): self.__px = px
    def set_v(self, vx): self.__vx = vx
    def reset(self, x0,v0): 
        self.__p0 = x0
        self.__px = x0
        self.__v0 = v0
        self.__vx = v0
        self.__t = 0

    # Evolve in time according to parablic motion
    def evolve(self,dt):
        self.__t += dt
        self.__vx = self.__vx - ball.__g * dt
        self.__px = self.__p0 + self.__v0 * self.__t - 0.5*ball.__g*self.__t**2