# Cdf of the detector response $X\sim\mathcal{N}(100, 25)$, with the probabilities read at $100\pm10$
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from preamble import *  # imports, rng, colours: see preamble.py

mu = 100
sigma = 5
x_range = np.array([90, 110])

p_above = 1 - norm.cdf(110, mu, sigma)
p_within = (norm.cdf(110, mu, sigma)
            - norm.cdf(90, mu, sigma))
print(f"P(X > 110) = {p_above:.4f}")
print(f"P(|X - 100| <= 10) = {p_within:.4f}")

x = np.linspace(80, 120, 400)
cdf_range = norm.cdf(x_range, mu, sigma)
fig, ax = plt.subplots()
ax.plot(x, norm.cdf(x, mu, sigma), color=col.cdf)
ax.vlines(x_range, 0, cdf_range, **thr)
ax.hlines(cdf_range, x[0], x_range, **thr)
ax.set_xlabel("$x$")
ax.set_ylabel("cdf")

plt.show()
