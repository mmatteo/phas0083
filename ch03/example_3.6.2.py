# Example 3.6.2 (Figure 3.16): Pdf and cdf of the exponential distribution with mean $\beta = 2$
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from preamble import *  # imports, rng, colours: see preamble.py

beta = 2
x = np.linspace(0, 5 * beta, 400)

pdf = expon.pdf(x, scale=beta)
cdf = expon.cdf(x, scale=beta)
p_above = 1 - expon.cdf(beta, scale=beta)
print(f"P(X > beta) = {p_above:.4f}")

fig, ax = plt.subplots()
ax.plot(x, pdf, color=col.pdf, label="pdf")
ax.plot(x, cdf, color=col.cdf, label="cdf")
ax.axvline(beta, color=col.ref, ls=":")
ax.set(xlabel="$x$", ylabel="$f(x)$, $F(x)$")
ax.legend()

plt.show()
