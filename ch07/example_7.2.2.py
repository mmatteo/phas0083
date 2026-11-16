# Example 7.2.2 (Figure 7.4): Probability of observing $x=3$ as a function of $\nu$, with its maximum
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from preamble import *  # imports, rng, colours: see preamble.py

x = 3
nu = np.linspace(0, 10, 101)
prob = poisson.pmf(x, nu)
prob_max = prob.max()
nu_best = nu[np.argmax(prob)]

fig, ax = plt.subplots()
ax.plot(nu, prob, "o", color=col.like, ms=3)
ax.hlines(prob_max, nu[0], nu_best, color=col.ref, ls=":")
ax.vlines(nu_best, 0, prob_max, color=col.ref, ls=":")
ax.set(xlabel=r"$\nu$", ylabel=rf"$P(X={x}\mid\nu)$")

plt.show()
