from numpy import cos,sin,pi

class Platform:
    '''
    Class for an oscillating platform
    '''

    # Constructor method
    def __init__(self, A=1, w=1,phi=0):
        self.pos=2*A
        self.vel=0
        self.A=A
        self.w=w
        self.phi=phi

    # Evolve in time as harmonic oscillator
    def evolve(self,dt):
        self.pos = self.A+self.A*cos(self.w*dt + self.phi)
        self.vel = -self.A*self.w*sin(self.w*dt + self.phi)
        self.phi +=dt*self.w

        # check that the phase goes back to 0
        while self.phi >= 2*pi:
            self.phi -= 2*pi