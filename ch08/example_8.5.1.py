# Example 8.5.1 (Figure 8.9): Simulated distribution of $-2\log\lambda$ for the one-sided test on the mean of a normal sample under $H_0$ (top) and its ecdf (bottom), with the level-0.05 threshold
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from preamble import *  # imports, rng, colours: see preamble.py

n = 5
theta_0 = 1.0
alpha = 0.05
m = 99_999


def nlrt(x_bar):
    return n * np.maximum(0, x_bar - theta_0)**2


# draw m samples under H0 and compute the statistic
x = rng.normal(theta_0, 1, size=(m, n))
x_bar = x.mean(axis=1)
T_sorted = np.sort(nlrt(x_bar))

# find the threshold at level alpha
c = T_sorted[round((m + 1) * (1 - alpha)) - 1]
print(f"threshold for level {alpha}:")
print(f"-2 log lambda > {c:.2f}")

fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)
ax1.hist(T_sorted, bins=60, density=True, color=col.hist)
ax1.axvline(c, color=col.ref, ls=":")
ax1.set(yscale="log", ylabel="density")
ax2.ecdf(T_sorted, color=col.draws)
ax2.axvline(c, color=col.ref, ls=":")
ax2.set(xlabel=r"$-2\log\lambda$", ylabel="ecdf")

plt.show()
