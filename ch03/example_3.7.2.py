# Example 3.7.2 (Figure 3.14): Pdf and cdf of the normal distribution $\mathcal{N}(0, 1)$
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from preamble import *  # imports, rng, colours: see preamble.py

mu = 0
sigma = 1
x = np.linspace(mu - 4 * sigma, mu + 4 * sigma, 400)

pdf = norm.pdf(x, mu, sigma)
cdf = norm.cdf(x, mu, sigma)

fig, ax = plt.subplots()
ax.plot(x, pdf, color=col.pdf, label="pdf")
ax.plot(x, cdf, color=col.cdf, label="cdf")
ax.set_xlabel("$x$")
ax.set_ylabel("$f(x)$, $F(x)$")
ax.legend()

plt.show()
