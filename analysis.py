import numpy as np

def interpolate_ground_impact(states):
    '''
    Uses linear interpolation to find when the projectile hits the ground in the middle of a timestep.
    Trim the states array to include before the timestep only.

    Parameters
    ----------
    states: an array of (x_pos, y_pos, x_vel, y_vel) states in chronological order

    Returns
    -------
    above_states: the input states array trimmed to include above ground indices and the final interpolated index
    '''
    below = np.where(states[:,1] < 0)[0]                     # Collect the indices of all states where y < 0

    #%% Interpolate to find the x position when the projectile reaches y = 0.
    if len(below) > 0:
        i = below[0]                                         # The first index below ground
        x1, y1 = states[i - 1, 0], states[i - 1, 1]          # The last x and y above ground
        x2, y2 = states[i, 0], states[i, 1]                  # The first x and y below ground
        alpha = y1 / (y1 - y2)                               # alpha: Fraction of the Euler step to travel in order to reach the ground
        x_ground = x1 + alpha * (x2 - x1)                    # The Euler step's estimate of x upon reaching the ground

    #%% Export a copy of the states array with above ground values only.
    above_states = states.copy()[:i+1,:]
    above_states[i,0] = x_ground
    above_states[i,1] = 0
    return above_states

def analytical_solution(start, stop, initial_position, initial_velocity):
    '''
    Calculates the analytical solution to the projectile equations of motion:
    x = x0 + Vx t
    y = y0 + Vy t - 0.5 g t^2
    Returns the x and y values of the projectile above ground according to the analytical solution.
    '''
    times = np.arange(start, stop, 0.01)
    x_analytical = initial_position[0] + initial_velocity[0] * times
    y_analytical = initial_position[1] + initial_velocity[1] * times - 4.9 * times**2
    mask = (y_analytical >= 0)                                           # Erase values where y < 0
    return x_analytical[mask], y_analytical[mask]

def error_analysis(step_sizes, estimate_ranges_list, analytical_range):
    '''
    Calculates the error of each estimate range compared to the analytical range
    Returns the errors in a list.
    '''
    errors_list = []
    for i in range(len(step_sizes)):
        error = estimate_ranges_list[i] - analytical_range
        errors_list.append(error)
    return errors_list
