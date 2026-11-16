# Example 5.1.8 (Figure 5.5): Marginal pmfs of the sum $X$ and the absolute difference $Y$ of two dice, summed from the joint pmf
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from preamble import *  # imports, rng, colours: see preamble.py

# joint pmf f(x, y) of the sum and the absolute difference
f = np.zeros((13, 6))
for d1 in range(1, 7):
    for d2 in range(1, 7):
        f[d1 + d2, abs(d1 - d2)] += 1 / 36

# marginal pmfs, summed over the other variable
f_X = f.sum(axis=1)
f_Y = f.sum(axis=0)
print(f"f_X(6) = {f_X[6]:.4f}")
print(f"f_Y(0) = {f_Y[0]:.4f}")

x = np.arange(2, 13)
y = np.arange(6)
fig, (ax1, ax2) = plt.subplots(2, 1)
ax1.plot(x, f_X[x], "o", color=col.pmf)
ax1.vlines(x, 0, f_X[x], colors=col.pmf)
ax1.set(xticks=x, xlabel="$x$", ylabel="$f_X(x)$")
ax2.plot(y, f_Y[y], "o", color=col.pmf)
ax2.vlines(y, 0, f_Y[y], colors=col.pmf)
ax2.set(xticks=y, xlabel="$y$", ylabel="$f_Y(y)$")

plt.show()
