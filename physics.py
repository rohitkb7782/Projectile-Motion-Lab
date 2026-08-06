import numpy as np

def get_derivative(position_and_velocity, t):
    '''
    Takes in the position and velocity of a projectile, packaged in one vector, and the current time. 
    Returns its velocity and acceleration, packaged in one vector

    Parameters
    ----------
    position_and_velocity: a four-element tuple or array (x_pos, y_pos, x_vel, y_vel) representing the current position and velocity state
    time: a float representing the current time

    Returns
    -------
    velocity_and_acceleration: a four-element array (x_vel, y_vel, x_acc, y_acc) representing the current velocity and acceleration
    '''
    #%% Set constants.
    g = 9.8                               # gravitational acceleration     [m/s^2]

    #%% Unpack the vector's components.
    x_pos = position_and_velocity[0]
    y_pos = position_and_velocity[1]
    x_vel = position_and_velocity[2]
    y_vel = position_and_velocity[3]

    #%% Compute the derivatives.
    velocity_and_acceleration = np.zeros(4)                 # Create a list to store derivatives.
    velocity_and_acceleration[2] = 0                        # x-acceleration
    velocity_and_acceleration[3] = -g                       # y-acceleration
    velocity_and_acceleration[0] = x_vel                    # x-velocity
    velocity_and_acceleration[1] = y_vel                    # y_velocity
    return velocity_and_acceleration