# Projectile Motion Simulation with Quadratic Drag

A Python-based computational physics project that simulates projectile motion using numerical integration. The project begins with ideal projectile motion and extends the model by incorporating quadratic air resistance.

## Motivation

Projectile motion provides a simple introduction to computational modeling because the underlying physics can be described using differential equations. The ideal projectile case has a known analytical solution, allowing numerical methods to be validated. Adding aerodynamic drag creates a more realistic system that requires numerical simulation.

This project explores how physical assumptions and numerical methods affect the predicted behavior of a system.

## Physics Model

The projectile is represented by the state vector:

$$
\mathbf{s} =
\begin{bmatrix}
x \\
y \\
v_x \\
v_y
\end{bmatrix}
$$

For ideal projectile motion:

$$
\frac{dx}{dt}=v_x
$$

$$
\frac{dy}{dt}=v_y
$$

$$
\frac{dv_x}{dt}=0
$$

$$
\frac{dv_y}{dt}=-g
$$

The drag model introduces a quadratic air resistance force:

$$
\mathbf{F}_d=-\frac{1}{2}C_d\rho A|\mathbf{v}|\mathbf{v}
$$

which produces accelerations:

$$
a_x=-\frac{c}{m}|\mathbf{v}|v_x
$$

$$
a_y=-g-\frac{c}{m}|\mathbf{v}|v_y
$$

where $c$ represents the combined drag coefficient terms.

## Numerical Method

The equations of motion are solved using Euler's Method:

$$
\mathbf{s}_{n+1}
=
\mathbf{s}_n+\Delta t\frac{d\mathbf{s}}{dt}
$$

The timestep size is varied to investigate numerical accuracy and convergence.

## Features

- Numerical simulation of projectile motion
- Ideal projectile and quadratic drag models
- Custom Euler integration solver
- Modular separation of physics, solvers, and analysis
- Ground-impact interpolation
- Numerical error analysis for the ideal case

## Project Structure

```
main.py       Runs simulations and visualization
physics.py    Defines physical models
solvers.py    Numerical integration methods
analysis.py   Error calculations and trajectory analysis
```

## Results



## Future Improvements

- Implement higher-order methods such as RK4
- Add wind forces
- Add gravity variation with height
