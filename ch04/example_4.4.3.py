# Example 4.4.3 (Figure 4.8): Q-Q plots of $N=10$ (top) and $N=100$ (bottom) draws from $\mathcal{N}(0,1)$ against the normal quantiles
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from preamble import *  # imports, rng, colours: see preamble.py

lims = [-4, 4]

fig, axes = plt.subplots(2, 1, sharex=True)
for ax, N in zip(axes, [10, 100]):
    x = np.sort(rng.normal(0, 1, N))
    # plotting positions
    p = (np.arange(1, N + 1) - 0.5) / N
    ax.plot(lims, lims, **ref)
    ax.plot(norm.ppf(p), x, "o", color=col.emp, ms=2)
    ax.set_xlim(lims)
    ax.set_ylim(lims)
    ax.set_title(f"$N={N}$")
    ax.set_ylabel("sample quantile")
axes[-1].set_xlabel("theoretical quantile")

plt.show()
