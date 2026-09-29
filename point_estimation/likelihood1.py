# Pmfs of the Poisson models with $\nu=3.0$ and $\nu=5.5$
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from preamble import *  # imports, rng, colours: see preamble.py

x = np.arange(0, 10)

fig, ax = plt.subplots()
for color, nu in zip(shades(col.pdf, 2), [3.0, 5.5]):
    pmf = poisson.pmf(x, nu)
    ax.plot(x, pmf, "o", color=color,
            label=rf"$\nu={nu}$")
    ax.vlines(x, 0, pmf, colors=[color])
ax.set_xlabel("$x$")
ax.set_ylabel("probability")
ax.legend()

plt.show()
