# Example 8.5.3 (Figure 8.11): Fraction of the $m$ simulated values of the likelihood-ratio statistic under $H_0$ equal to each value, the discrete counterpart of the histogram of Figure~\ref{fig:hypothesis_testing/lrt-normal-margin} (top), and their ecdf (bottom), with the level-0.05 threshold
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from preamble import *  # imports, rng, colours: see preamble.py

nu = 50
alpha = 0.05
m = 99_999


def nlrt(x, nu):
    lam_hat = np.maximum(0, x - nu)
    return (-2 * poisson.logpmf(x, nu)
            + 2 * poisson.logpmf(x, lam_hat + nu))


# draw m counts under H0 and compute the statistic
x = rng.poisson(nu, size=m)
T_sorted = np.sort(nlrt(x, nu))
# count how often each value of the statistic occurs
t_values, counts = np.unique(T_sorted, return_counts=True)
fraction = counts / m

# find the threshold at level alpha
c = T_sorted[round((m + 1) * (1 - alpha)) - 1]
print(f"threshold for level {alpha}:")
print(f"-2 log lambda > {c:.3f}")

fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)
ax1.plot(t_values, fraction, "o", color=col.hist, ms=4)
ax1.vlines(t_values, 0, fraction, colors=col.hist, lw=2)
ax1.axvline(c, color=col.ref, ls=":")
ax1.set(yscale="log", ylabel="fraction of simulations")
ax2.ecdf(T_sorted, color=col.draws)
ax2.axvline(c, color=col.ref, ls=":")
ax2.set(xlabel=r"$-2\log\lambda$", ylabel="ecdf")

plt.show()
