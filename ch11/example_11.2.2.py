# Example 11.2.2 (Figure 11.1): ecdf of the decay times and cdf of the fitted exponential model (top); Q-Q plot of the decay times against the fitted model (bottom)
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from preamble import *  # imports, rng, colours: see preamble.py

x = np.array([3.54, 5.13, 2.84, 4.48, 1.03, 16.92,
              0.05, 14.05, 2.88, 1.50, 2.71, 1.56])
n = x.size

x_bar = x.mean()

# Q-Q plot: probabilities (i - 1/2) / n of the sorted data
p = (np.arange(1, n + 1) - 0.5) / n

u = np.linspace(0, 20, 200)
fig, (ax1, ax2) = plt.subplots(2, 1)
ax1.ecdf(x, color=col.data, label="ecdf")
ax1.plot(u, expon.cdf(u, scale=x_bar), color=col.cdf,
         label="fitted exponential")
ax1.set(xlabel=r"decay time [$\mu$s]", ylabel="cdf")
ax1.legend()
ax2.plot(u, u, color=col.ref, ls="--")
ax2.plot(expon.ppf(p, scale=x_bar), np.sort(x), "o",
         color=col.data, ms=3)
ax2.set_xlabel(r"fitted quantile [$\mu$s]")
ax2.set_ylabel(r"decay time [$\mu$s]")

plt.show()
