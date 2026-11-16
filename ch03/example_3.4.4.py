# Example 3.4.4 (Figure 3.9): Pmf and cdf of the binomial distribution with $n=10$, $p=0.3$
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from preamble import *  # imports, rng, colours: see preamble.py

n = 10
p = 0.3
y = np.arange(0, n + 1)
pmf = binom.pmf(y, n, p)
cdf = binom.cdf(y, n, p)

fig, ax = plt.subplots()
ax.plot(y, pmf, "o", color=col.pmf, label="pmf")
ax.vlines(y, 0, pmf, colors=col.pmf)
ax.plot(y, cdf, "o", color=col.cdf, label="cdf")
ax.hlines(cdf, y, y + 1, colors=col.cdf)
ax.set(xticks=y, xlabel="$y$", ylabel="probability")
ax.legend()

plt.show()
