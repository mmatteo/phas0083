# Example 8.2.2 (Figure 8.1): EDF of the decay times and cdf of the fitted exponential model
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from preamble import *  # imports, rng, colours: see preamble.py

x = np.array([3.54, 5.13, 2.84, 4.48, 1.03, 16.92,
              0.05, 14.05, 2.88, 1.50, 2.71, 1.56])
n = x.size
x_bar = x.mean()

# cdf of the fitted exponential model
u = np.linspace(0, 20, 200)
F_fit = stats.expon.cdf(u, scale=x_bar)

fig, ax = plt.subplots()
ax.ecdf(x, color=col.emp, label="EDF")   # steps of 1/n
ax.plot(u, F_fit, color=col.cdf, label="fitted exponential")
ax.set_xlabel(r"decay time [$\mu$s]")
ax.set_ylabel("cdf")
ax.legend()

plt.show()
