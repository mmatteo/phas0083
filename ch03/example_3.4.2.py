# Example 3.4.2 (Figure 3.7): Pmf and cdf of a Bernoulli random variable with $p=2/3$
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from preamble import *  # imports, rng, colours: see preamble.py

p = 2 / 3
x = np.array([0, 1])
pmf = np.array([1 - p, p])
cdf = np.cumsum(pmf)

fig, ax = plt.subplots()
ax.plot(x, pmf, "o", color=col.pdf, label="pmf")
ax.vlines(x, 0, pmf, colors=col.pdf)
ax.plot(x, cdf, "o", color=col.cdf, label="cdf")
ax.hlines(cdf, x, x + 1, colors=col.cdf)
ax.set_xticks(x)
ax.set_xlabel("$x$")
ax.set_ylabel("probability")
ax.legend()

plt.show()
