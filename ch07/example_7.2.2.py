# Example 7.2.2 (Figure 7.6): Probability of observing $x=3$ as a function of $\nu$, with its maximum
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from preamble import *  # imports, rng, colours: see preamble.py

nu = np.linspace(0, 10, 101)
x = 3
likelihood = poisson.pmf(x, nu)
nu_best = nu[np.argmax(likelihood)]

fig, ax = plt.subplots()
ax.plot(nu, likelihood, "o", color=col.like, ms=3)
ax.hlines(likelihood.max(), nu.min(), nu_best, **thr)
ax.vlines(nu_best, 0, likelihood.max(), **thr)
ax.set_xlabel(r"$\nu$")
ax.set_ylabel(r"$P(X=3\mid\nu)$")

plt.show()
