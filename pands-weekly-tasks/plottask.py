# plottask.py
## This program displays a histogram of a normal distribution of a 1000 values with a mean of 5 and a standard deviation of 2, and a plot of the function h(x) = x3 in the range 0 to 10. Both plots are displayed on the same set of axes and saved as a PNG image file.
## Author: Leah Curran

# Using the numpy method demonstrated in the useful modules lecture, did some further reading on it [1]: 
import numpy as np
import matplotlib.pyplot as plt

# Make results repeatable each time the program runs - setting a random seeds ensures that the same random values are egnerated every time the program runs.
np.random.seed(0)

# 1. Normal distribution - Defining the parameters, generate 1000 random values following a normal distribution
mean = 5
std_dev = 2
sample_size = 1000

data = np.random.normal(mean, std_dev, sample_size)


# 2. Generate data for the Function h(x) = x^3  (evenly spaced values between 0 and 10, linspace used to create a smooth curve), calculate corresponding y values
x = np.linspace(0, 10, 400)
y = x ** 3


# 3. Plotting - crerating a reasonable size so all elements are easy to read

plt.figure(figsize=(8, 6))

# 4. Histogram (normalised so it fits nicely with the line plot), representing probability instead of raw counts for readability (done originally on raw counts and it was a mess).
# Used an LLM to talk me through the design elements [5]: 
plt.hist(
    data,
    bins=30,
    density=True,
    alpha=0.6,
    label="Normal Distribution (mean=5, std=2)"
)

# 5. Scale x^3 so it fits on the same axes as the histogram
plt.plot(
    x,
    y / max(y),
    color="red",
    linewidth=2,
    label="h(x) = x³ (scaled)"
)

# 6. Labels and styling - Adding title, legend and axis labels 
plt.title("Normal Distribution Histogram and h(x) = x³")
plt.xlabel("Value")
plt.ylabel("Density / Scaled Value")
plt.legend()
plt.grid(True)

# 7. Save plot to file - to include in repository
plt.savefig("plottask.png")
plt.close()

print("Plot saved as plottask.png")

# [1] Further reading on Numpy: NumPy Documentation – Random Sampling
# https://numpy.org/doc/stable/reference/random/generated/numpy.random.normal.html


# NumPy Documentation – linspace
# https://numpy.org/doc/stable/reference/generated/numpy.linspace.html


# Matplotlib Documentation – Histograms
# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.hist.html


# Matplotlib Documentation – Plotting Lines
# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html

# [5] LLM Conversation on histogram design: https://m365.cloud.microsoft/chat/?fromCode=cmcv2&redirectId=D9355808C958483BBE56620D01A398DA&login_hint=leah.curran1%40abbott.com&internalredirect=CCM&client-request-id=5662cce2-e961-4658-9923-89cab8addad6&origindomain=CCM