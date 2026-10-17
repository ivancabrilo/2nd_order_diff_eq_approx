import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


g = 9.8 # gravity
L = 5 # length of the pendulum
THETA_0 = np.pi/2 
THETA_DOT_0 = 0 # inital angular veloctiy is 0
mu = 0.1


# change in theta can be approximated by delta_theta = theta_dot * delta_t
# for sufficiently small time interval
# so now i can just find new_theta = old_theta + delta_theta
# applies to everything that changes continously 
#  
def get_theta_double_dot(theta, theta_dot):
    return (-mu*theta_dot - (g/L)*np.sin(theta))

def theta(t):
    x_positions = []
    y_positions = []
    theta_angles = []
    theta = THETA_0
    theta_dot = THETA_DOT_0
    delta_t = 0.01

    
    for time in np.arange(0, t, delta_t):
        theta_double_dot = get_theta_double_dot(theta, theta_dot)
        theta_dot += theta_double_dot * delta_t
        theta += theta_dot * delta_t
        x_positions.append(L*np.sin(theta))
        y_positions.append(-L*np.cos(theta))
        theta_angles.append(np.rad2deg(theta))
        # print(f"Theta in degrees {np.rad2deg(theta)}")
        
    return x_positions,y_positions, theta_angles

x_positions, y_positions, theta_angles = theta(t=200)


fig, ax = plt.subplots()

x1 = 0
y1 = 0
x2 = x_positions[0]
y2 = y_positions[0]

rod, = ax.plot([x1,x2],[x2,y2],'-o')

ax.plot(x_positions, y_positions, linewidth=2.0)
ax.set(xlim=(-7, 7), xticks=np.arange(-6, 7), ylim=(-7,7), yticks=np.arange(-6, 7))
ax.set_aspect('equal')
angle_label = ax.text(
    0.98, 0.95, "",
    transform=ax.transAxes,
    ha="right",
    va="top"
)

def update(i):
    rod.set_data([0, x_positions[i]], [0, y_positions[i]])
    angle_label.set_text(f"θ = {theta_angles[i]:.1f}°")
ani = FuncAnimation(fig, update, frames=len(x_positions), interval=0.1)

ani.save("pendulum.gif", writer="pillow", fps=30)

plt.show()
plt.close()
