# Example 3.7.5 (Figure 3.20): Poisson pmf for increasing $\nu$, and the normal approximation for $\nu=40$
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from preamble import *  # imports, rng, colours: see preamble.py

nu_max = 40
x = np.arange(0, 60)
mu = nu_max
sigma = np.sqrt(nu_max)
u = np.linspace(0, 60, 400)

fig, ax = plt.subplots()
for color, nu in zip(shades(col.pmf, 3), [5, 20, nu_max]):
    pmf = poisson.pmf(x, nu)
    ax.plot(x, pmf, "o", color=color, label=rf"$\nu={nu}$")
    ax.vlines(x, 0, pmf, colors=color)
ax.plot(u, norm.pdf(u, mu, sigma), color=col.ref, ls="--",
        label="normal")
ax.set(xlabel="$x$", ylabel="probability")
ax.legend()

plt.show()
