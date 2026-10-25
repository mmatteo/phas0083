# Example 11.2.3 (Figure 11.7): Bootstrap distribution of the test statistic under $H_0$ for $\lambda_0=100$, $10$, $5$ and $0$ (top to bottom) with $\nu=10$, the $\chi^2_1$ prediction and the level-0.05 thresholds
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from preamble import *  # imports, rng, colours: see preamble.py

# -2 log likelihood ratio of the on/off model, with the
# MLE of lambda kept at or above zero
def nlrt(x, lambda_0, nu):
    lambda_hat = np.maximum(0, x - nu)
    return (-2 * poisson.logpmf(x, lambda_0 + nu)
            + 2 * poisson.logpmf(x, lambda_hat + nu))


nu = 10
alpha = 0.05
B = 1_000_000
bins = np.linspace(0, 15, 51)
centres = (bins[:-1] + bins[1:]) / 2
# the chi-squared probability of each bin, per unit width
chi2_density = np.diff(chi2.cdf(bins, df=1)) / np.diff(bins)

fig, axes = plt.subplots(4, 1, sharex=True)
for ax, lambda_0 in zip(axes, [100, 10, 5, 0]):
    # the simulated statistic under H0 and the threshold,
    # the (B + 1)(1 - alpha)-th ordered value
    x_star = rng.poisson(lambda_0 + nu, size=B)
    T_sorted = np.sort(nlrt(x_star, lambda_0, nu))
    c = T_sorted[int((B + 1) * (1 - alpha)) - 1]
    print(f"lambda_0 = {lambda_0:4d}: threshold {c:.2f}")
    ax.hist(T_sorted, bins=bins, density=True,
            color=col.hist)
    ax.plot(centres, chi2_density, **ref)
    ax.axvline(c, **thr)
    ax.set_yscale("log")
    ax.set_ylim(1e-6, 5)
    ax.set_title(f"$\\lambda_0={lambda_0}$")
    ax.set_ylabel("density")
axes[-1].set_xlabel(r"$\tilde\lambda$")

plt.show()
