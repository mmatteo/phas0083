# Example 3.4.5 (Figure 3.9): Binomial pmf for $n=5,10,20$ at $p=0.5$ (top) and for $p=0.1,0.2,0.6$ at $n=20$ (bottom)
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from preamble import *  # imports, rng, colours: see preamble.py

def binom_modes(n, p):
    """Modes of a binomial: two if (n+1)p is an integer."""
    m = (n + 1) * p
    if abs(m - round(m)) < 1e-12:
        return int(m - 1), int(m)
    return (int(np.floor(m)),)


cases = [[(5, 0.5), (10, 0.5), (20, 0.5)],   # fixed p
         [(20, 0.1), (20, 0.2), (20, 0.6)]]  # fixed n

fig, axes = plt.subplots(2, 1, sharex=True)
for ax, row in zip(axes, cases):
    for color, (n, p) in zip(shades(col.pdf, 3), row):
        x = np.arange(n + 1)
        pmf = binom.pmf(x, n, p)
        modes = ", ".join(map(str, binom_modes(n, p)))
        label = f"$n={n}$, $p={p}$: mode {modes}"
        ax.vlines(x, 0, pmf, colors=[color])
        ax.plot(x, pmf, "o", color=color, label=label)
    ax.set_ylabel("probability")
    ax.legend()
axes[1].set_xlabel("number of successes")

print("Binomial modes, two when (n+1)p is an integer:")
for n, p in cases[0] + cases[1]:
    print(f"  n={n:2d}, p={p}: {binom_modes(n, p)}")

plt.show()
