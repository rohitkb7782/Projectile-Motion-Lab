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