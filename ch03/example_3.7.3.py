# Example 3.7.3 (Figure 3.18): Cdf of the detector response $X\sim\mathcal{N}(100, 25)$, with the probabilities read at $100\pm10$
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from preamble import *  # imports, rng, colours: see preamble.py

mu = 100
sigma = 5
a, b = 90, 110

F_a, F_b = norm.cdf([a, b], mu, sigma)
print(f"P(X > {b}) = {1 - F_b:.4f}")
print(f"P(|X - {mu}| <= {b - mu}) = {F_b - F_a:.4f}")

x = np.linspace(mu - 4 * sigma, mu + 4 * sigma, 400)
fig, ax = plt.subplots()
ax.plot(x, norm.cdf(x, mu, sigma), color=col.cdf)
ax.vlines([a, b], 0, [F_a, F_b], color=col.ref, ls=":")
ax.hlines([F_a, F_b], x[0], [a, b], color=col.ref, ls=":")
ax.set(xlabel="$x$", ylabel="cdf")

plt.show()
