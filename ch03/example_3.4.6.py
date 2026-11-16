# Example 3.4.6 (Figure 3.11): Pmf and cdf of the number of detected gamma-rays, binomial with $n=20$, $p=0.1$
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from preamble import *  # imports, rng, colours: see preamble.py

n = 20
p = 0.1
y = np.arange(0, n + 1)
pmf = binom.pmf(y, n, p)
cdf = binom.cdf(y, n, p)

print(f"P(Y = 1) = {binom.pmf(1, n, p):.4f}")
print(f"P(Y >= 1) = {1 - binom.cdf(0, n, p):.4f}")
print(f"P(Y < 1) = {binom.cdf(0, n, p):.4f}")

fig, ax = plt.subplots()
ax.plot(y, pmf, "o", color=col.pmf, label="pmf")
ax.vlines(y, 0, pmf, colors=col.pmf)
ax.plot(y, cdf, "o", color=col.cdf, label="cdf")
ax.hlines(cdf, y, y + 1, colors=col.cdf)
ax.set(xlabel="$y$", ylabel="probability")
ax.legend()

plt.show()
