import numpy as np

class World(object):
    """
    Class to contain the world. This will assume a
    flat Earth with a ground position 
    (default at y = 1 meter)
    """

    def __init__(self):
        self.ground_height = 1.0

class Particle(World):
    """
    Particle class as a child of World. Particles in
    freefall. Will include a method to compute collisions.
    Border will default within 0.1 meters.
    Default timestep dt will be dt = 0.1 s.
    Take gravity as g = 9.81 m/s^2.
    """

    """
    x0, y0, vx0 = 0.0, vy0 = 0.0,
    dt = 0.05, duration = 10.0, drag_coeff = 0.0, damp = 1.0
    """
    
    def __init__(self, **kwargs):
        super().__init__()

        #particle kinematic state and timestep
        #keep as a single vector of pos and vel
        self.init_state = np.array([kwargs["x0"], kwargs["y0"], kwargs["vx0"], kwargs["vy0"]])
        self.dt = kwargs["dt"]
        self.t = kwargs["duration"]
        self.t0 = 0.0

        #array to contain states at each timestep
        self.timeline = np.empty((4, len(np.arange(self.t0, self.t, self.dt))))
        self.timeline[:, 0] = self.init_state

        #dampening coefficients for linear air drag and inelastic collision
        self.dampen = kwargs["damp"]
        self.b = kwargs["drag_coeff"]

    def simulate(self):
        #euler computational simulation
        #loop over the simulation time
        for i in range(1, len(np.arange(self.t0, self.t, self.dt))):
            #check for collision with the ground
            #border of 0.1
            if (self.timeline[1, i - 1] <= (self.ground_height + 0.1)) & (self.timeline[3, i - 1] < 0.0):
                #set state to previous time
                self.advance_collision(i)
            else:
                self.freefall_calc(i)

    def freefall_calc(self, i):
        #calculate the advance vector with g and vel
        #advance change in particle state
        #set state to previous time
        g = -9.81

        self.timeline[3, i] = self.timeline[3, i - 1] + g * self.dt - self.b * self.timeline[3, i - 1] * self.dt
        self.timeline[2, i] = self.timeline[2, i - 1] - self.b * self.timeline[2, i - 1] * self.dt
        self.timeline[0, i] = self.timeline[0, i - 1] + self.timeline[2, i - 1] * self.dt
        self.timeline[1, i] = self.timeline[1, i - 1] + self.timeline[3, i - 1] * self.dt
        
    def advance_collision(self, i):
        #advance motion according to a collision
        self.timeline[3, i] = -1 * self.dampen * self.timeline[3, i - 1]
        self.timeline[2, i] = self.dampen * self.timeline[2, i - 1]
        self.timeline[0, i] = self.timeline[0, i - 1] + self.timeline[2, i - 1] * self.dt
        self.timeline[1, i] = self.timeline[1, i - 1] + self.timeline[3, i - 1] * self.dt
        