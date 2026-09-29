# Pmf and cdf of the binomial distribution with $n=10$, $p=0.3$
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from preamble import *  # imports, rng, colours: see preamble.py

n = 10
p = 0.3
x = np.arange(0, n + 1)
pmf = binom.pmf(x, n, p)
cdf = binom.cdf(x, n, p)

fig, ax = plt.subplots()
ax.plot(x, pmf, "o", color=col.pdf, label="pmf")
ax.vlines(x, 0, pmf, colors=col.pdf)
ax.plot(x, cdf, "o", color=col.cdf, label="cdf")
ax.hlines(cdf, x, x + 1, colors=col.cdf)
ax.set_xlabel("$x$")
ax.set_ylabel("probability")
ax.legend()

plt.show()
