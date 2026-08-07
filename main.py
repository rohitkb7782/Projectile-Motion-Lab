import numpy as np
import matplotlib.pyplot as plt
from physics import projectile_derivative, projectile_drag_derivative
from analysis import interpolate_ground_impact, analytical_solution, error_analysis
from solvers import euler_solver

#%% Initialize parameters.
start = 0
stop = 5

estimate_ranges_list = []                                            # List to store each simulation's estimate of the projectile's range
initial_position = (0, 0)                                            # initial x- and y- positions    [m]
initial_velocity = (5, 10)                                           # initial x- and y- velocities   [m/s]
model = "drag"

if model == "ideal":
    #%% Run the simulation at different step sizes
    step_sizes = [0.001, 0.01, 0.1, 0.3, 0.5]                            # Compare simulation accuracy when different step sizes are used
    for step in step_sizes:
        times = np.arange(start, stop + step, step)                      # times at which to evaluate position and velocity   [s]
        initial_state = initial_position + initial_velocity              # Concatenate initial conditions into a 4D vector
        states = euler_solver(projectile_derivative, initial_state, times)           # Solve for the 4D vector at the specified times
        above_states = interpolate_ground_impact(states)
    
        #%% Unpack the states vectors
        x_positions = above_states[:,0]
        y_positions = above_states[:,1]
        x_velocities = above_states[:,2]
        y_velocities = above_states[:,3]

        estimate_ranges_list.append(x_positions[-1])
        plt.plot(x_positions, y_positions, label=str(step)+" s")

    #%% Calculate the analytical solution to the initial value problem
    x_analytical, y_analytical = analytical_solution(start, stop, initial_position, initial_velocity)
    plt.plot(x_analytical, y_analytical, "--", label="Analytical Solution")
    analytical_range = x_analytical[-1]

    plt.xlabel("Horizontal Distance [m]")
    plt.ylabel("Vertical Height [m]")
    plt.title("Projectile Motion using Euler's Method with different step sizes")
    plt.legend()

    #%% Compare the analytical range to the estimate ranges and compute errors.
    print("Step size\tRange estimate\tError")
    print(f"Analytical\t{analytical_range:.2f} m")
    errors_list = error_analysis(step_sizes, estimate_ranges_list, analytical_range)
    for i in range(len(step_sizes)):
        print(f"{step_sizes[i]} s\t\t{estimate_ranges_list[i]:.2f} m\t\t{errors_list[i]:.2f} m")

    plt.figure()
    plt.plot(step_sizes, errors_list)
    plt.xlabel("Step Sizes [s]")
    plt.ylabel("Errors in Range [m]")
    plt.title("Errors in Range vs. Step Sizes for Euler's Method")

elif model == "drag":
    #%% Run the simulation at step size 0.001 s
    times = np.arange(start, stop + 0.001, 0.001)                    # times at which to evaluate position and velocity   [s]
    initial_state = initial_position + initial_velocity              # Concatenate initial conditions into a 4D vector
    states = euler_solver(projectile_drag_derivative, initial_state, times)           # Solve for the 4D vector at the specified times
    above_states = interpolate_ground_impact(states)
    
    #%% Unpack the states vectors
    x_positions = above_states[:,0]
    y_positions = above_states[:,1]
    x_velocities = above_states[:,2]
    y_velocities = above_states[:,3]

    plt.plot(x_positions, y_positions, label="Quadratic Drag (Numerically Computed)")

    #%% Calculate the analytical solution to the initial value problem
    x_analytical, y_analytical = analytical_solution(start, stop, initial_position, initial_velocity)
    plt.plot(x_analytical, y_analytical, "--", label="Analytical Solution")
    
    plt.xlabel("Horizontal Distance [m]")
    plt.ylabel("Vertical Height [m]")
    plt.title("Projectile Motion with vs. without Quadratic Drag")
    plt.legend()
    plt.savefig("drag_vs_ideal.png")
