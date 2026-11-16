# Example 3.7.4 (Figure 3.19): Binomial pmf with $p=0.3$ for increasing $n$, and the normal approximation for $n=100$
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from preamble import *  # imports, rng, colours: see preamble.py

p = 0.3
n_max = 100
x = np.arange(0, 45)
mu = n_max * p
sigma = np.sqrt(n_max * p * (1 - p))
u = np.linspace(0, 45, 400)

fig, ax = plt.subplots()
for color, n in zip(shades(col.pmf, 3), [10, 30, n_max]):
    pmf = binom.pmf(x, n, p)
    ax.plot(x, pmf, "o", color=color, label=f"$n={n}$")
    ax.vlines(x, 0, pmf, colors=color)
ax.plot(u, norm.pdf(u, mu, sigma), color=col.ref, ls="--",
        label="normal")
ax.set(xlabel="$x$", ylabel="probability")
ax.legend()

plt.show()
