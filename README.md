# Projectile Motion Simulation

This project simulates the motion of a projectile using **Euler's Method** and compares the numerical solution to the analytical solution.

## Features

- Simulates 2D projectile motion under constant gravity
- Implements Euler's Method for numerical integration
- Uses linear interpolation to estimate the projectile's landing position
- Compares numerical results with the analytical solution
- Investigates the effect of timestep size on numerical accuracy

## Files

| File | Description |
|------|-------------|
| `main.py` | Runs the simulation, generates plots, and computes errors |
| `physics.py` | Defines the projectile's equations of motion |
| `solvers.py` | Implements Euler's Method |
| `analysis.py` | Contains helper functions such as ground-impact interpolation |
| `requirements.txt` | Lists required Python packages |

## Requirements

- Python 3
- NumPy
- Matplotlib

Install dependencies with:

```bash
pip install -r requirements.txt
```

## Running the Project

Run the simulation with:

```bash
python main.py
```

The program will:
- Plot projectile trajectories for several timestep sizes.
- Plot the analytical solution.
- Display the numerical error in the estimated range.

## Example Output

The simulation generates:
- Projectile trajectories
- Error versus timestep plots
- Estimated projectile ranges

## Author

Your Name
