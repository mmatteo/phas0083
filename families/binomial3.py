# Pmf and cdf of the number of detected gamma-rays, binomial with $n=20$, $p=0.1$
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from preamble import *  # imports, rng, colours: see preamble.py

n = 20
p = 0.1
x = np.arange(0, n + 1)
pmf = binom.pmf(x, n, p)
cdf = binom.cdf(x, n, p)

fig, ax = plt.subplots()
ax.plot(x, pmf, "o", color=col.pdf, label="pmf")
ax.vlines(x, 0, pmf, colors=col.pdf)
ax.plot(x, cdf, "o", color=col.cdf, label="cdf")
ax.hlines(cdf, x, x + 1, colors=col.cdf)
ax.set_xlabel("$y$")
ax.set_ylabel("probability")
ax.legend()

print(f"P(Y = 1) = {binom.pmf(1, n, p):.4f}")
print(f"P(Y >= 1) = {1 - binom.cdf(0, n, p):.4f}")
print(f"P(Y < 1) = {binom.cdf(0, n, p):.4f}")

plt.show()
