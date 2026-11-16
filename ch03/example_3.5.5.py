# Example 3.5.5 (Figure 3.14): Cdf of the Poisson distribution with $\nu=10$
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from preamble import *  # imports, rng, colours: see preamble.py

nu = 10
n = np.arange(0, 21)
cdf = poisson.cdf(n, nu)

p_le5 = poisson.cdf(5, nu)
p_10to15 = poisson.cdf(15, nu) - poisson.cdf(9, nu)
print(f"P(N <= 5 | nu={nu}) = {p_le5:.4f}")
print(f"P(10 <= N <= 15 | nu={nu}) = {p_10to15:.4f}")

fig, ax = plt.subplots()
ax.plot(n, cdf, "o", color=col.cdf)
ax.hlines(cdf, n, n + 1, colors=col.cdf)
ax.set(xlabel="$n$", ylabel="cdf")

plt.show()
