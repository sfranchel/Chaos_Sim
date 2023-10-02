import matplotlib.pyplot as plt
import Simulator.ChaoticSystem as CS
from ipywidgets import GridspecLayout, widgets, Layout
from numpy import pi 

#Disable inline plots
plt.ioff()

#Define the Grid
GRID_HEIGHT=500.
GRID_WIDTH=950.

# Physical system parameters
b_v0 = widgets.FloatText(value=0.12,step=1e-2, description='Ball v0 [m/s]', layout=Layout(height='auto', width='auto'))
b_x0 = widgets.FloatText(value=1.2,step=1e-1, description='Ball x0 [mm]', layout=Layout(height='auto', width='auto'))
b_A0 = widgets.FloatText(value=0.41,step=1e-2, description='Ampl. [mm]', layout=Layout(height='auto', width='auto'))
b_f0 = widgets.FloatText(value=30,step=1e-2, description='Freq. [1/s]', layout=Layout(height='auto', width='auto'))
b_mu = widgets.FloatSlider(value=0.7, min=0, max=1, step=0.01, description='Res. factor',layout=Layout(height='auto', width='auto'))

# Simulation parameters
b_dt = widgets.FloatLogSlider(value=1e-4, base=10,step=0.2,min=-6, max=-2, description='dt [s]',layout=Layout(height='auto', width='auto'))
b_n_dt = widgets.IntSlider(value=10000, min=1, max=3e4, description='Steps',layout=Layout(height='auto', width='auto'))

# Run button and output window
b_run = widgets.Button(description='Run', layout=Layout(height='auto', width='auto'))
output = widgets.Output(layout=Layout(height='auto', width='auto'))


def plot_evolution_static(x0,v0,A,w,mu,dt,n_dt,scale=[1000,'mm']):
    # Initialize the system 
    c=CS.ChaoticSystem(x0,v0,A,w,mu)
  
    # Initialize arrays
    xcb = [c.get_ball_x()*scale[0]]
    xcp = [c.get_platform_x()*scale[0]]
    t = [0]

    # Run the simulation
    for i in range(n_dt):
        c.evolve(dt)
        t.append(t[i]+dt)
        xcb.append(c.get_ball_x()*scale[0])
        xcp.append(c.get_platform_x()*scale[0])

    # Plot the results
    fig, ax = plt.subplots(1,1,figsize=((GRID_WIDTH)/100*(2./3),(GRID_HEIGHT)/100), )
    ax.plot(t,xcb, label='Ball')
    ax.plot(t,xcp, label='Platform')
    ax.set_title('Simulation')
    ax.legend()
    ax.set_xlabel('time [s]')
    ax.set_ylabel(f'displacement [{scale[1]}]')

    return fig.canvas


# Define the button  click function
def on_button_clicked(b):
    with output:
        output.clear_output()
        display(plot_evolution_static(
                              b_x0.value*1e-3, # mm
                              b_v0.value,      # m/s
                              b_A0.value*1e-3, # mm
                              b_f0.value*2*pi, # 1/s
                              b_mu.value,
                              b_dt.value,
                              b_n_dt.value,
                             ))

# Assignit to the button click event
b_run.on_click(on_button_clicked)

# Initialize the GUI itself
GUI = GridspecLayout(8,3, height=f'{GRID_HEIGHT}px', width=f'{GRID_WIDTH}px',align_items='center')

GUI[0,0]= b_run
GUI[1,0]= b_x0
GUI[2,0]= b_v0
GUI[3,0]= b_A0
GUI[4,0]= b_f0
GUI[5,0]= b_mu
GUI[6,0]= b_dt
GUI[7,0]= b_n_dt
GUI[:,1:]= output

