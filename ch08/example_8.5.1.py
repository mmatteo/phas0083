# Example 8.5.1 (Figure 8.8): Simulated distribution of the likelihood-ratio statistic under $H_0$ (top) and its survival function (bottom), with the level-0.05 threshold
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from preamble import *  # imports, rng, colours: see preamble.py

# -2 log of the likelihood ratio for H0: lambda = 0, with
# the background nu known and the MLE of lambda kept at
# or above zero
def nlrt(x, nu):
    lambda_hat = np.maximum(0, x - nu)
    return (-2 * poisson.logpmf(x, nu)
            + 2 * poisson.logpmf(x, lambda_hat + nu))


nu = 50
alpha = 0.05
m = 100_000

# the ensemble under H0: m counts from the background alone
x = rng.poisson(nu, size=m)
T_sorted = np.sort(nlrt(x, nu))

# the threshold: the (m + 1)(1 - alpha)-th ordered value
c = T_sorted[int((m + 1) * (1 - alpha)) - 1]
print(f"threshold for level 0.05: -2 log lambda > {c:.3f}")

fig, axes = plt.subplots(2, 1, sharex=True)
axes[0].hist(T_sorted, density=True, bins=40, color=col.hist)
axes[0].set_yscale("log")
axes[0].set_ylabel("density")
survival = np.linspace(1, 0, m, endpoint=False)
axes[1].plot(T_sorted, survival, color=col.cdf)
axes[1].set_ylabel("survival")
axes[1].set_xlabel(r"$-2\log\lambda$")
for ax in axes:
    ax.axvline(c, **thr)

plt.show()
