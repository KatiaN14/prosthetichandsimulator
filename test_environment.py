# Test script to verify the environment
import numpy as np
import scipy as sp
import pandas as pd
import matplotlib
import sklearn
from sklearn import datasets

print("NumPy version:", np.__version__)
print("SciPy version:", sp.__version__)
print("Pandas version:", pd.__version__)
print("Matplotlib version:", matplotlib.__version__)
print("Scikit-learn version:", sklearn.__version__)

# Test a simple plot
import matplotlib.pyplot as plt
x = np.linspace(0, 10, 100)
y = np.sin(x)
plt.plot(x, y)
plt.title("Test Plot")
plt.savefig("test_plot.png")  # Save the plot to a file
plt.close()

print("All libraries imported successfully!")