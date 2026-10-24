# Example 3.4.5 (Figure 3.9): Binomial pmf for $n=5,10,20$ at $p=0.5$ (top) and for $p=0.1,0.2,0.6$ at $n=20$ (bottom)
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from preamble import *  # imports, rng, colours: see preamble.py

# fixed p = 0.5 (top), fixed n = 20 (bottom)
cases = [[(5, 0.5), (10, 0.5), (20, 0.5)],
         [(20, 0.1), (20, 0.2), (20, 0.6)]]

fig, axes = plt.subplots(2, 1, sharex=True)
for ax, row in zip(axes, cases):
    for color, (n, p) in zip(shades(col.pdf, 3), row):
        x = np.arange(n + 1)
        pmf = binom.pmf(x, n, p)
        modes = x[pmf == pmf.max()]
        print(f"n={n}, p={p}: (n+1)p = {(n + 1) * p},"
              f" mode {modes}")
        ax.vlines(x, 0, pmf, colors=[color])
        ax.plot(x, pmf, "o", color=color,
                label=f"$n={n}$, $p={p}$")
    ax.set_ylabel("probability")
    ax.legend()
axes[1].set_xlabel("number of successes")

plt.show()
