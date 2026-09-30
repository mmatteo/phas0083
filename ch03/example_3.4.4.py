# Example 3.4.4 (Figure 3.7): Binomial pmf for $n=5,10,20$ at $p=0.5$ (top) and for $p=0.1,0.2,0.6$ at $n=20$ (bottom)
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from preamble import *  # imports, rng, colours: see preamble.py

def binom_mode(n, p):
    """Mode from the pmf, and the closed-form candidates."""
    x = np.arange(n + 1)
    pmf = binom.pmf(x, n, p)
    mode = x[np.argmax(pmf)]
    candidates = (int(np.floor((n + 1) * p)),
                  int(np.ceil((n + 1) * p) - 1))
    return mode, candidates, x, pmf


cases = [[(5, 0.5), (10, 0.5), (20, 0.5)],   # fixed p
         [(20, 0.1), (20, 0.2), (20, 0.6)]]  # fixed n

fig, axes = plt.subplots(2, 1, sharex=True)
for ax, row in zip(axes, cases):
    for color, (n, p) in zip(shades(col.pdf, 3), row):
        mode, _, x, pmf = binom_mode(n, p)
        label = f"$n={n}$, $p={p}$: mode {mode}"
        ax.vlines(x, 0, pmf, colors=[color])
        ax.plot(x, pmf, "o", color=color, label=label)
    ax.set_ylabel("probability")
    ax.legend()
axes[1].set_xlabel("number of successes")

print("mode from the pmf; floor((n+1)p), ceil((n+1)p)-1")
for n, p in cases[0] + cases[1]:
    mode, (c1, c2), _, _ = binom_mode(n, p)
    print(f"n={n:2d}, p={p}: {mode:2d}; {c1:2d}, {c2:2d}")

plt.show()
