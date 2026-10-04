# Example 3.7.5 (Figure 3.19): Poisson pmf for increasing $\nu$, and the normal approximation for $\nu=40$
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from preamble import *  # imports, rng, colours: see preamble.py

x = np.arange(0, 60)

fig, ax = plt.subplots()
for color, nu in zip(shades(col.pdf, 3), [5, 20, 40]):
    pmf = poisson.pmf(x, nu)
    ax.plot(x, pmf, "o", color=color,
            label=rf"$\nu={nu}$")
    ax.vlines(x, 0, pmf, colors=[color])

mu = 40
sigma = np.sqrt(40)
u = np.linspace(0, 60, 400)
ax.plot(u, norm.pdf(u, mu, sigma), **ref, label="normal")
ax.set_xlabel("$x$")
ax.set_ylabel("probability")
ax.legend()

plt.show()
