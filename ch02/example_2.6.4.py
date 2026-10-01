# Example 2.6.4 (Figure 2.8): Pmf and cdf of the score of a fair die
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from preamble import *  # imports, rng, colours: see preamble.py

x = np.arange(0, 7)
pmf = np.array([0] + [1 / 6] * 6)
cdf = np.cumsum(pmf)

fig, ax = plt.subplots()
ax.plot(x, pmf, "o", color=col.pdf, label="pmf")
ax.vlines(x, 0, pmf, colors=col.pdf)
ax.plot(x, cdf, "o", color=col.cdf, label="cdf")
ax.hlines(cdf, x, x + 1, colors=col.cdf)
ax.set_xlabel("$x$")
ax.set_ylabel("probability")
ax.legend()

plt.show()
