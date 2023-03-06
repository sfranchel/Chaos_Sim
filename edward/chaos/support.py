import numpy as np


class Support:
    def __init__(self, A: float, f: float, z0: float) -> None:
        """
        Support class. It has the following parameters :

        Parameters:
        ---
        - A : Amplitude
        - f : Fréquence (Hz)
        - z0 : Hauteur initiale
        """
        self.A = A
        self.f = f
        self.z0 = z0

        self.pos_vals: np.ndarray
        self.velX : np.ndarray
        # self.time_vals: np.ndarray

    def compute_positions(self, t) -> None:
        # self.time_vals = np.arange(tmax, dt)
        self.pos_vals = self.A * np.sin(2 * np.pi * self.f * t) + self.z0
        self.velX = self.A * np.cos(2 * np.pi * self.f * t) * 2 * np.pi * self.f
        
        # print("pos_val_support création",self.pos_vals)

    def get_sliced_positions(self, i, j):
        return self.pos_vals[i:j]
    

    
