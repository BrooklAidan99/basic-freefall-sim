from objects import Particle
import matplotlib.pyplot as plt
import matplotlib.animation as animation

params = {"x0" : 5.0, "y0" : 10.0, "vx0" : 10.0, "vy0" : 0.0, 
          "dt" : 0.05, "duration" : 10.0, "damp" : 0.8, "drag_coeff" : 0.1}

ball = Particle(**params)
ball.simulate()

#positions along x and y directions
x = ball.timeline[0, :]
y = ball.timeline[1, :]

#animate the ball
fig = plt.figure()
ax = fig.add_subplot(111)
a = ax.plot([x[0]], [y[0]], marker = 'o')
b = ax.hlines(y = ball.ground_height - 0.2, xmin = 0.0, xmax = (max(x) + 5.0))
ax.set_xlabel('x [m]')
ax.set_ylabel('y [m]')
ax.set_xlim(left = 0.0, right = (max(x) + 5.0))
ax.set_ylim(top = 15.0, bottom = -2.0)

#define animation function (just cycling through the positions in timeline)
def animate(i):
    a[0].set_data([x[i + 1]], [y[i + 1]])

ani = animation.FuncAnimation(fig, animate, interval = 0, frames = len(x) - 1, repeat = True)

plt.show()
