# Example 3.3.2 (Figure 3.6): Pmf and cdf of the discrete uniform on $\{1,\dots,6\}$ (top); pdf and cdf of the continuous uniform on $(0,2)$ (bottom)
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from preamble import *  # imports, rng, colours: see preamble.py

fig, axes = plt.subplots(2, 1)

# discrete: the score of a die
x = np.arange(1, 7)
pmf = np.full(6, 1 / 6)
cdf = np.cumsum(pmf)
axes[0].vlines(x, 0, pmf, colors=col.pdf)
axes[0].plot(x, pmf, "o", color=col.pdf, label="pmf")
axes[0].plot(x, cdf, "o", color=col.cdf, label="cdf")
axes[0].hlines(cdf, x, x + 1, colors=col.cdf)
axes[0].set_xticks(x)
axes[0].set_xlabel("$x$")

# continuous: uniform on (a, b)
a, b = 0, 2
u = np.linspace(-0.5, 2.5, 400)
pdf = np.where((u >= a) & (u <= b), 1 / (b - a), 0)
cdf = np.clip((u - a) / (b - a), 0, 1)
axes[1].plot(u, pdf, color=col.pdf, label="pdf")
axes[1].plot(u, cdf, color=col.cdf, label="cdf")
axes[1].set_xlabel("$x$")
for ax in axes:
    ax.set_ylabel("probability")
    ax.legend()

plt.show()
