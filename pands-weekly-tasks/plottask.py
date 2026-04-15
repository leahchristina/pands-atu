# plottask.py
## This program displays a histogram of a normal distribution of a 1000 values with a mean of 5 and a standard deviation of 2, and a plot of the function h(x) = x3 in the range 0 to 10.
## Author: Leah Curran

import numpy as np
import matplotlib.pyplot as plt

# Make results repeatable each time the program runs
np.random.seed(0)

# -----------------------------
# Part 1: Normal distribution
# -----------------------------
mean = 5
std_dev = 2
sample_size = 1000

data = np.random.normal(mean, std_dev, sample_size)

# -----------------------------
# Part 2: Function h(x) = x^3
# -----------------------------
x = np.linspace(0, 10, 400)
y = x ** 3

# -----------------------------
# Plotting
# -----------------------------
plt.figure(figsize=(8, 6))

# Histogram (normalised so it fits nicely with the line plot)
plt.hist(
    data,
    bins=30,
    density=True,
    alpha=0.6,
    label="Normal Distribution (mean=5, std=2)"
)

# Scale x^3 so it fits on the same axes as the histogram
plt.plot(
    x,
    y / max(y),
    color="red",
    linewidth=2,
    label="h(x) = x³ (scaled)"
)

# Labels and styling
plt.title("Normal Distribution Histogram and h(x) = x³")
plt.xlabel("Value")
plt.ylabel("Density / Scaled Value")
plt.legend()
plt.grid(True)

# Save plot to file
plt.savefig("plottask.png")
plt.close()

print("Plot saved as plottask.png")