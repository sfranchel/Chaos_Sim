'''  '''
from numpy import cos

def Bisection_solver(dt, x0,v0, A0,w0,phi0, tol=1e-4,max_iter=100):
    '''
    Find intersection between parabola and sinusoidal function,
    with Bisection method.
    Parameters are:
    dt = range where the interception is supposed to be
    x0, v0 = parameters of the parabola
    A, w, phi  = parameters of the cos function
    tol = tolerance in time granularity, with respect to the considered time interval dt
    '''
    # define f(t)
    def f(t):
        return (x0+v0*t - 0.5*9.80665*t**2) - (A0+A0*cos(t*w0 + phi0))

    tmax=0
    tmin=-dt
    n_iter=0

    while (tmax - tmin)*0.5 > tol*dt and max_iter:
        n_iter+=1

        tavg = (tmin + tmax)*0.5

        # if the middle point is the intersection, return tavg
        if f(tavg) == 0:
            return tavg
        # if f(t) changes sign between tmin and tavg, set tmax -> tavg
        elif f(tmin) * f(tavg) < 0:
            tmax = tavg
        # else f(t0)=0 is in the other half of the interval, set tmin -> tavg
        else:
            tmin = tavg

    return (tmin + tmax) / 2
