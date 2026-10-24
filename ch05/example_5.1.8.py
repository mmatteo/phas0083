# Example 5.1.8 (Figure 5.4): Marginal pmfs of the sum $X$ and the absolute difference $Y$ of two dice, summed from the joint pmf
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from preamble import *  # imports, rng, colours: see preamble.py

# joint pmf f(x, y) of the sum and the absolute difference
f = np.zeros((13, 6))
for d1 in range(1, 7):
    for d2 in range(1, 7):
        f[d1 + d2, abs(d1 - d2)] += 1 / 36

# marginal pmfs, summed over the other variable
f_X, f_Y = f.sum(axis=1), f.sum(axis=0)
print(f"f_X(6) = {f_X[6]:.4f}")
print(f"f_Y(0) = {f_Y[0]:.4f}")

x = np.arange(2, 13)
y = np.arange(6)
fig, axes = plt.subplots(2, 1)
axes[0].vlines(x, 0, f_X[x], colors=col.pdf)
axes[0].plot(x, f_X[x], "o", color=col.pdf)
axes[0].set_xlabel("$x$")
axes[0].set_ylabel("$f_X(x)$")
axes[1].vlines(y, 0, f_Y[y], colors=col.pdf)
axes[1].plot(y, f_Y[y], "o", color=col.pdf)
axes[1].set_xlabel("$y$")
axes[1].set_ylabel("$f_Y(y)$")

plt.show()
