# Example 5.1.8 (Figure 5.4): Marginal pmfs of the sum $X$ and the absolute difference $Y$ of two dice, summed from the joint pmf
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from preamble import *  # imports, rng, colours: see preamble.py

f = np.zeros((13, 6))   # joint pmf f[x, y], by the values
for d1 in range(1, 7):
    for d2 in range(1, 7):
        f[d1 + d2, abs(d1 - d2)] += 1 / 36

f_X = f.sum(axis=1)          # summed over y
f_Y = f.sum(axis=0)          # summed over x
print(f"f_X(6) = {f_X[6]:.4f}")
print(f"f_Y(0) = {f_Y[0]:.4f}")

x = np.arange(2, 13)         # the values of the sum
y = np.arange(6)             # the values of the difference
fig, axes = plt.subplots(2, 1)
for ax, v, f_v, n in zip(axes, [x, y], [f_X, f_Y], "xy"):
    ax.vlines(v, 0, f_v[v], colors=col.pdf)
    ax.plot(v, f_v[v], "o", color=col.pdf)
    ax.set_xlabel(f"${n}$")
    ax.set_ylabel(f"$f_{n.upper()}({n})$")

plt.show()
