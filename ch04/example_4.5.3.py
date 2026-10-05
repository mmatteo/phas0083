# Example 4.5.3 (Figure 4.8): Distance of simulated photons from a point source: histogram, KDE and the true Rayleigh pdf
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from preamble import *  # imports, rng, colours: see preamble.py

sigma = 1.0
N = 5000
x = rng.normal(0, sigma, N)
y = rng.normal(0, sigma, N)
r = np.sqrt(x**2 + y**2)

kde = gaussian_kde(r)
u = np.linspace(0, r.max(), 300)
f_true = u / sigma**2 * np.exp(-u**2 / (2 * sigma**2))

fig, ax = plt.subplots()
ax.hist(r, bins=40, density=True, color=col.hist,
        label="histogram")
ax.plot(u, kde(u), color=col.emp, label="KDE")
ax.plot(u, f_true, **ref, label="Rayleigh")
ax.set_xlabel("$r$")
ax.set_ylabel("density")
ax.legend()

plt.show()
