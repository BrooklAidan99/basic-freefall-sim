Simple simulation of a particle in free fall using the Euler scheme. Linear air drag is incorporated into the calculations as well as simple collision detection with the ground.
Input to the simulation takes the following quantities: 
x0, y0 - initial x and y position of the particle; 
vx0, vy0 - initial velocity components of the particle; 
dt - the time step for the simulation
duration - the duration of the simulation
damp - coefficient to model inelastic collisions with the ground, effectively decreases the velocity on impact
drag_coeff - linear air drag coefficient
