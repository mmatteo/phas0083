# Example 3.3.2 (Figure 3.6): Pmf and cdf of the discrete uniform on $\{0,\dots,9\}$ (top); pdf and cdf of the continuous uniform on $(0,2)$ (bottom)
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from preamble import *  # imports, rng, colours: see preamble.py

# discrete uniform on {0, ..., 9}
x = np.arange(0, 10)
pmf = np.full(x.size, 1 / x.size)
cdf_x = np.cumsum(pmf)

# continuous uniform on (a, b)
a = 0
b = 2
u = np.linspace(a - 0.5, b + 0.5, 400)
inside = (u >= a) & (u <= b)
pdf = np.where(inside, 1 / (b - a), 0)
cdf_u = np.clip((u - a) / (b - a), 0, 1)

fig, (ax1, ax2) = plt.subplots(2, 1)
ax1.plot(x, pmf, "o", color=col.pmf, label="pmf")
ax1.vlines(x, 0, pmf, colors=col.pmf)
ax1.plot(x, cdf_x, "o", color=col.cdf, label="cdf")
ax1.hlines(cdf_x, x, x + 1, colors=col.cdf)
ax1.set(xticks=x, xlabel="$x$", ylabel="probability")
ax1.legend()
ax2.plot(u, pdf, color=col.pdf, label="pdf")
ax2.plot(u, cdf_u, color=col.cdf, label="cdf")
ax2.set(xlabel="$x$", ylabel="probability")
ax2.legend()

plt.show()
