# Example 3.7.4 (Figure 3.16): Binomial pmf with $p=0.3$ for increasing $n$, and the normal approximation for $n=100$
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from preamble import *  # imports, rng, colours: see preamble.py

p = 0.3
x = np.arange(0, 45)

fig, ax = plt.subplots()
for color, n in zip(shades(col.pdf, 3), [10, 30, 100]):
    pmf = binom.pmf(x, n, p)
    ax.plot(x, pmf, "o", color=color, label=f"$n={n}$")
    ax.vlines(x, 0, pmf, colors=[color])

mu = 100 * p
sigma = np.sqrt(100 * p * (1 - p))
u = np.linspace(0, 45, 400)
ax.plot(u, norm.pdf(u, mu, sigma), **ref, label="normal")
ax.set_xlabel("$x$")
ax.set_ylabel("probability")
ax.legend()

plt.show()
