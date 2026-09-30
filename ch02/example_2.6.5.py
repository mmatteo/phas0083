# Example 2.6.5 (Figure 2.12): Pdf and cdf of the standard normal distribution
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from preamble import *  # imports, rng, colours: see preamble.py

x = np.linspace(-4, 4, 100)

fig, ax = plt.subplots()
ax.plot(x, norm.pdf(x), color=col.pdf, label="pdf")
ax.plot(x, norm.cdf(x), color=col.cdf, label="cdf")
ax.set_xlabel("$x$")
ax.set_ylabel("$f(x)$, $F(x)$")
ax.legend()

plt.show()
