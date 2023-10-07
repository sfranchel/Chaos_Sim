from ipywidgets import GridspecLayout, widgets, Layout
import matplotlib.pyplot as plt
import Simulator.ChaoticSystem as CS
import numpy as np

#Disable inline plots
plt.ioff()

#Define the Grid
GRID_HEIGHT=500.
GRID_WIDTH=950.

# Physical system parameters
b_v0 = widgets.FloatText(value=0.12,step=1e-2, description='Ball v0 [m/s]', layout=Layout(height='auto', width='auto'))
b_x0 = widgets.FloatText(value=1.2,step=1e-1, description='Ball x0 [mm]', layout=Layout(height='auto', width='auto'))
b_f0 = widgets.FloatText(value=30,step=1e-1, description='Freq. [1/s]', layout=Layout(height='auto', width='auto'))
b_mu = widgets.FloatSlider(value=0.5, min=0, max=1, step=0.01, description='Res. factor',layout=Layout(height='auto', width='auto'))
b_A_range = widgets.FloatRangeSlider(value = [0.380, 0.551], step=0.001, min=0.2, max=1.0, description='A range [mm]', layout=Layout(height='auto', width='auto'))


# Simulation parameters
b_dt = widgets.FloatLogSlider(value=1e-4, base=10,step=0.2,min=-6, max=-2, description='dt:',layout=Layout(height='auto', width='auto'))
b_n_dt = widgets.IntSlider(value=10000, min=1, max=2e4, description='dt steps:',layout=Layout(height='auto', width='auto'))
b_n_A = widgets.IntSlider(value=100, min=1, max=1000, description='A steps:',layout=Layout(height='auto', width='auto'))

# Run button and output window
b_run = widgets.Button(description='Run', layout=Layout(height='auto', width='auto'))
output = widgets.Output(layout=Layout(height='auto', width='auto'))
p_bar = widgets.FloatProgress( value=0, description='Running:', bar_style='info', layout=Layout(height='auto', width='auto'))

def simulate_bifurcation(x0,v0,w,mu,A_range,n_A, dt,n_dt, pbar):
    # Initialize the system 
    c=CS.ChaoticSystem(x0,v0,A_range[0],w,mu)
  
    phi_arr=[]
    A_arr=[]

    pbar.min=A_range[0]
    pbar.max=A_range[1]
    pbar.value=A_range[0]

    # Loop over the amplitudes
    print("Setting range to: ",A_range[0],A_range[1],n_A)
    for A in np.linspace(A_range[0],A_range[1],n_A):
        pbar.value=A
        c.set_platform_A(A)
        c.reset()

        for i in range(n_dt):
            c.evolve(dt)

        # Fill arrays
        A_arr.append([A for j in range(len(c.t_coll))])
        phi_arr.append(c.phi_coll)

    # Plot the results
    fig, ax = plt.subplots(1,1,figsize=((GRID_WIDTH)/100*(2./3),(GRID_HEIGHT)/100*(7./9)), )

    for i in range(len(phi_arr)): 
        ax.scatter(np.array(A_arr[i][10:])*1e3,phi_arr[i][10:],c='k',s=0.1)

    ax.set_title('Simulation of Phase Bifurcation')
    ax.set_ylabel('phase [periods]')
    ax.set_xlabel('Amplitude [mm]')

    return fig.canvas


# Define the button  click function
def on_button_clicked(b):
    with output:
        output.clear_output()
        display(simulate_bifurcation(
                              b_x0.value*1e-3,
                              b_v0.value,
                              b_f0.value*2*np.pi,
                              b_mu.value,
                              [x*1e-3 for x in  b_A_range.value],
                              b_n_A.value,
                              b_dt.value,
                              b_n_dt.value,
                              p_bar,
                             ))

# Assignit to the button click event
b_run.on_click(on_button_clicked)

# Initialize the GUI itself
GUI = GridspecLayout(9,3, height=f'{GRID_HEIGHT}px', width=f'{GRID_WIDTH}px',align_items='center')

GUI[0,0]= b_run
GUI[1,0]= b_x0
GUI[2,0]= b_v0
GUI[3,0]= b_f0
GUI[4,0]= b_mu
GUI[5,0]= b_A_range
GUI[6,0]= b_n_A
GUI[7,0]= b_dt
GUI[8,0]= b_n_dt
GUI[:7,1:]= output
GUI[8,1:]= p_bar

