import numpy as np
import matplotlib.pyplot as plt

from physics import get_derivative
from solvers import euler_solver
from analysis import interpolate_ground_impact

#%% Initialize parameters.
start = 0
stop = 5
step_sizes = [0.001, 0.01, 0.1, 0.3, 0.5]                            # Compare simulation accuracy when different step sizes are used
estimate_ranges_list = []                                            # List to store each simulation's estimate of the projectile's range
initial_position = (0, 0)                                            # initial x- and y- positions    [m]
initial_velocity = (5, 10)                                           # initial x- and y- velocities   [m/s]

#%% Run the simulation at different step sizes
for step in step_sizes:
    times = np.arange(start, stop + step, step)                      # times at which to evaluate position and velocity   [s]
    initial_state = initial_position + initial_velocity              # Concatenate initial conditions into a 4D vector
    states = euler_solver(get_derivative, initial_state, times)      # Solve for the 4D vector at the specified times
    above_states = interpolate_ground_impact(states)

    #%% Unpack the states vectors
    x_positions = above_states[:,0]
    y_positions = above_states[:,1]
    x_velocities = above_states[:,2]
    y_velocities = above_states[:,3]

    estimate_ranges_list.append(x_positions[-1])
    plt.plot(x_positions, y_positions, label=str(step)+" s")

#%% Calculate the analytical solution to the initial value problem.
times = np.arange(start, stop, 0.01)
x_analytical = initial_position[0] + initial_velocity[0] * times
y_analytical = initial_position[1] + initial_velocity[1] * times - 4.9 * times**2
mask = (y_analytical >= 0)                                           # Erase values where y < 0
x_analytical, y_analytical = x_analytical[mask], y_analytical[mask]
plt.plot(x_analytical, y_analytical, "--", label="Analytical Solution")

plt.xlabel("Horizontal Distance [m]")
plt.ylabel("Vertical Height [m]")
plt.title("Projectile Motion using Euler's Method with different step sizes")
plt.legend()

#%% Compare the analytical range to the estimate ranges and compute errors.
analytical_range = x_analytical[-1]
print("Step size\tRange estimate\tError\n---------\t--------------\t-----")
print(f"Analytical\t{analytical_range:.2f} m")

errors_list = []
for i in range(len(step_sizes)):
    estimate_range = estimate_ranges_list[i]
    error = estimate_range - analytical_range
    errors_list.append(error)
    print(f"{step_sizes[i]} s\t\t{estimate_range:.2f} m\t\t{error:.2f} m")

plt.figure()
plt.plot(step_sizes, errors_list)
plt.xlabel("Step Sizes [s]")
plt.ylabel("Errors in Range [m]")
plt.title("Errors in Range vs. Step Sizes for Euler's Method")