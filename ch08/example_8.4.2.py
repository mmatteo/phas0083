# Example 8.4.2 (Figure 8.4): Estimated 0.05 and 0.95 quantiles of $t^*-t$ against $B$
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from preamble import *  # imports, rng, colours: see preamble.py

x = np.array([3.54, 5.13, 2.84, 4.48, 1.03, 16.92,
              0.05, 14.05, 2.88, 1.50, 2.71, 1.56])
n = x.size
x_bar = x.mean()
B_values = [19, 39, 99, 199, 399, 599, 799, 999]

fig, ax = plt.subplots()
for color in shades(col.emp, 4):  # four independent runs
    q05, q95 = [], []
    for B in B_values:
        x_star = rng.exponential(scale=x_bar, size=(B, n))
        d = np.sort(x_star.mean(axis=1)) - x_bar
        q05.append(d[int((B + 1) * 0.05) - 1])
        q95.append(d[int((B + 1) * 0.95) - 1])
    ax.plot(B_values, q05, "o-", color=color)
    ax.plot(B_values, q95, "o-", color=color)

# exact: the mean of n exponentials is Gamma(n, x_bar/n)
for p in [0.05, 0.95]:
    q = stats.gamma.ppf(p, n, scale=x_bar / n) - x_bar
    ax.axhline(q, **ref)
ax.set_xscale("log")
ax.set_xlabel("$B$")
ax.set_ylabel("quantiles of $t^* - t$")

plt.show()
