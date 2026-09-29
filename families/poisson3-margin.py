# Cdf of the Poisson distribution with $\nu=10$
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from preamble import *  # imports, rng, colours: see preamble.py

nu = 10
x = np.arange(0, 21)
cdf = poisson.cdf(x, nu)

p_le5 = poisson.cdf(5, nu)
p_10to15 = poisson.cdf(15, nu) - poisson.cdf(9, nu)
print(f"P(N <= 5 | nu=10) = {p_le5:.4f}")
print(f"P(10 <= N <= 15 | nu=10) = {p_10to15:.4f}")

fig, ax = plt.subplots()
ax.plot(x, cdf, "o", color=col.cdf)
ax.hlines(cdf, x, x + 1, colors=col.cdf)
ax.set_xlabel("$n$")
ax.set_ylabel("cdf")

plt.show()
