# Example 11.5.1 (Figure 11.5): Bootstrap estimates of the bias (top) and variance (bottom) of the mean against $B$, in four runs
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from preamble import *  # imports, rng, colours: see preamble.py

x = np.array([3.54, 5.13, 2.84, 4.48, 1.03, 16.92,
              0.05, 14.05, 2.88, 1.50, 2.71, 1.56])
n = x.size
x_bar = x.mean()
B_values = [10, 20, 50, 100, 200, 500, 1000, 2000]

fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)
# repeat the simulation four times at every B
for color in shades(col.draws, 4):
    bias_B = []
    var_B = []
    for B in B_values:
        # compute bias and variance of the replicates
        x_star = rng.exponential(scale=x_bar, size=(B, n))
        t_star = x_star.mean(axis=1)
        bias_B.append(t_star.mean() - x_bar)
        var_B.append(t_star.var(ddof=1))
    ax1.plot(B_values, bias_B, "o-", color=color)
    ax2.plot(B_values, var_B, "o-", color=color)

# exact values under the fitted model
ax1.axhline(0, color=col.ref, ls="--")
ax2.axhline(x_bar**2 / n, color=col.ref, ls="--")
ax1.set_ylabel("bias")
ax2.set(xscale="log", xlabel="$B$", ylabel="variance")

plt.show()
