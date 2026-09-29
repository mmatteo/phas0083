# Histograms of the bootstrap replicates $t^*_i$ of the sample mean, for $B=99$ (top) and $B=999$ (bottom)
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from preamble import *  # imports, rng, colours: see preamble.py

x = np.array([3.54, 5.13, 2.84, 4.48, 1.03, 16.92,
              0.05, 14.05, 2.88, 1.50, 2.71, 1.56])
n = x.size
x_bar = x.mean()

fig, axes = plt.subplots(2, 1, sharex=True)
for ax, B in zip(axes, [99, 999]):
    # B bootstrap samples of size n from the fitted model
    x_star = rng.exponential(scale=x_bar, size=(B, n))
    t_star = x_star.mean(axis=1)
    ax.hist(t_star, density=True, color=col.hist)
    ax.set_title(f"$B={B}$")
    ax.set_ylabel("density")
axes[-1].set_xlabel("$t^*$")

plt.show()
