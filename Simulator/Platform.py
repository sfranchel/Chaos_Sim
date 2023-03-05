from numpy import cos,sin

class platform:
    '''
    Class for an oscillating platform
    '''

    # Constructor method
    def __init__(self, A=1, w=1,phi=0):
        self.__px=2*A
        self.__vx=0
        self.__A=A
        self.__w=w
        self.__phi=phi

    def __str__(self):
        __str  = f'Platform:\n'
        __str += f'\tpx={self.__px:.7f}, vx={self.__vx:.7f}\n' 
        __str += f'\tA={self.__A:.7f}, w={self.__w:.7f}, phi={self.__phi:.7f}'
        return __str

    # Get methods
    def get_x(self): return self.__px
    def get_v(self): return self.__vx
    def get_A(self): return self.__A
    def get_w(self): return self.__w
    def get_phi(self): return self.__phi

    # Set methods
    def set_A(self, A): self.__A=A
    def set_w(self, w): self.__w=w
    def reset(self,A=None,w=None): 
        self.__phi=0
        if A is not None: self.__A=A
        if w is not None: self.__w=w
        # evolve to update position and velocity
        self.evolve(0)

    # Evolve in time as harmonic oscillator
    def evolve(self,dt):
        self.__px = self.__A+self.__A*cos(self.__w*dt + self.__phi)
        self.__vx = -self.__A*self.__w*sin(self.__w*dt + self.__phi)
        self.__phi+=dt*self.__w