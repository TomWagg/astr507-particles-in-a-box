""" Use this file to test your simulator by visualising the results and making sure everything looks okay """
import simulator

# you probably want the size to be at least 750 as this is in pixels for the visualisation
size = 1000

# change these to valid values
E = None
mass = None
radius = None
N = None
steps = None

sim = simulator.Simulation(N=N, E=E, radius=radius, size=size, masses=mass, delay=20, visualise=True)
sim.run_simulation(steps)
