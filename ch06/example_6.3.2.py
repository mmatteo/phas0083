# Example 6.3.2 (Figure 6.8): Running sample mean of three samples from an exponential distribution with $\beta=1/2$
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from preamble import *  # imports, rng, colours: see preamble.py

beta = 1 / 2
N = 10_000
samples = [rng.exponential(scale=beta, size=N)
           for _ in range(3)]
n = np.arange(1, N + 1)

fig, ax = plt.subplots()
for color, x in zip(shades(col.emp, 3), samples):
    ax.plot(n, np.cumsum(x) / n, color=color)
ax.axhline(beta, **ref)
ax.set_xscale("log")
ax.set_xlabel("sample size $n$")
ax.set_ylabel(r"$\hat{\beta}_n$")

plt.show()
