import numpy as np
from numba import int32, float32    # import the types
from numba.experimental import jitclass


class Support :   
    def __init__(self, A:float, f:float, x0:float, absorbance = 1.) -> None:
        """
        Support class. It has the following parameters :
        
        Parameters:
        ---
        
        - A : Amplitude
        - f : Fréquence (Hz)
        - z0 : Hauteur initiale
        - up : Si le support est en phase ascendante ou descendante
        -> vitesse ? dérivée de la position ?
        """
        self.A  = A
        self.f = f
        self.x = 0
        self.v = 0
        self.x0 = x0
        self.absorbance =  absorbance
    
    def update(self,t):
        self.v = self.A * np.cos(2* np.pi * self.f * t + 0) * 2* np.pi * self.f
        self.x = self.A * np.sin(2*np.pi*self.f * t + 0) + self.x0
        
        
        
        
        
        
        
        
    

    
    
    