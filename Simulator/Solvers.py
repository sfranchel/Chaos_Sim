'''  '''
import numpy as np

def Bisection_solver(dt,x0,v0,A0,w0,phi0, tolerance=1e-8, max_iter=1000):
    '''
    Find intersection between parabola and sinusoidal function,
    with Bisection method method.
    Parameters are:
    dt = range where the interception is supposed to be
    x0, v0, t = parameters of the parabola
    A, w, phi  = parameters of the cos function
    '''
    # define f(t)
    def f(t):
        return (x0+v0*t - 0.5*9.80665*t**2) - (A0+A0*np.cos(t*w0 + phi0))
    b=dt
    a=-dt
    n_iter=0
    while (b - a) / 2 > tolerance and max_iter:
        n_iter+=1
        c = (a + b) / 2
        if f(c) == 0:
            return c
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return (a + b) / 2

def Newton_solver(dt, x0,v0,t, A,w,phi, tolerance=1e-6, max_iter=10000,debug=-1):
    '''
    Find intersection between parabola and sinusoidal function,
    with Newton–Raphson method.
    Parameters are:
    dt = range where the interception is supposed to be
    x0, v0, t = parameters of the parabola
    A, w, phi  = parameters of the cos function
    '''

    # define f(x)
    def f(x):
        return (x0+v0*(t+x) - 0.5*9.80665*(t+x)**2) - (A+A*np.cos(x*w + phi)) 

    if f(0)*f(dt)>0:
        print('warning 0 or more than 1 root expected !')
        if(debug>1):
          print('cosine:')
          print(A+A*np.cos(phi), A+A*np.cos(dt*w + phi))
          print('parabola:')
          print((x0+v0*t- 0.5*9.80665*(t)**2),(x0+v0*(t+dt) - 0.5*9.80665*(t+dt)**2))
          print('function in the extremes of interval:')
          print(f(0),f(dt))

        if f(-dt)*f(2*dt)>0:
            print('warning 0 or more than 1 root expected in extended interval !!!')


    # define derivative of f(x)
    def df(x): 
        return (v0 - 9.80665*(t+x))-(-A*w*np.sin(w*x + phi))

    result = -9999
    n_outer_iter = 0
    while result> dt*2 or result<-dt :
        if n_outer_iter > max_iter:
            raise ArithmeticError('Solver could not find any solution!!!')
        # define the x_k 
        t1=np.random.uniform(0,dt)
        t0=-1

        n_iter=0

        while abs(t0-t1) > tolerance:
            if n_iter > max_iter:
                raise ArithmeticError('Solver could not find any solution!!!')
            t0=t1
            t1=t0 - (f(t0)/df(t0))
            n_iter+=1
            #print('Iterations done:', n_iter)

        result = t1
        n_outer_iter += 1 

    return result