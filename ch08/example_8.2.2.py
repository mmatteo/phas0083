# Example 8.2.2 (Figure 8.1): ecdf of the decay times and cdf of the fitted exponential model (top); Q-Q plot of the decay times against the fitted model (bottom)
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from preamble import *  # imports, rng, colours: see preamble.py

x = np.array([3.54, 5.13, 2.84, 4.48, 1.03, 16.92,
              0.05, 14.05, 2.88, 1.50, 2.71, 1.56])
n = x.size

# the fitted model: the exponential with mean x_bar
x_bar = x.mean()

fig, (ax1, ax2) = plt.subplots(2, 1)
t = np.linspace(0, 20, 200)
ax1.ecdf(x, color=col.emp, label="ecdf")
ax1.plot(t, expon.cdf(t, scale=x_bar), **ref,
         label="fitted exponential")
ax1.set_xlabel(r"decay time [$\mu$s]")
ax1.set_ylabel("cdf")
ax1.legend()

# Q-Q plot: the sorted data against the quantiles of the
# fitted model at the probabilities (i - 1/2) / n
p = (np.arange(1, n + 1) - 0.5) / n
ax2.plot([0, 20], [0, 20], **ref)
ax2.plot(expon.ppf(p, scale=x_bar), np.sort(x), "o",
         color=col.emp, ms=3)
ax2.set_xlabel(r"fitted quantile [$\mu$s]")
ax2.set_ylabel(r"decay time [$\mu$s]")

plt.show()
