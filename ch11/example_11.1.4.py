# Example 11.1.4 (Figure 11.1): Bootstrap distribution of the test statistic under $H_0$, the chi-squared prediction and the level-0.05 threshold
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from preamble import *  # imports, rng, colours: see preamble.py

# -2 log likelihood ratio of the on/off model, with the
# MLE of lambda kept at or above zero
def nlrt(x, lambda_0, nu):
    lambda_hat = np.maximum(0, x - nu)
    return (-2 * poisson.logpmf(x, lambda_0 + nu)
            + 2 * poisson.logpmf(x, lambda_hat + nu))


lambda_0 = 1000
nu = 1000
alpha = 0.05
B = 1_000_000
# the simulated statistic under H0 and the threshold, the
# (B + 1)(1 - alpha)-th ordered value
x_star = rng.poisson(lambda_0 + nu, size=B)
T_sorted = np.sort(nlrt(x_star, lambda_0, nu))
threshold = T_sorted[int((B + 1) * (1 - alpha)) - 1]
print(f"level {alpha}: reject if T > {threshold:.3f}")

fig, ax = plt.subplots()
bins = np.linspace(0, 15, 51)
ax.hist(T_sorted, bins=bins, density=True, color=col.hist)
# the chi-squared probability of each bin, per unit width
chi2_density = np.diff(chi2.cdf(bins, df=1)) / np.diff(bins)
centres = (bins[:-1] + bins[1:]) / 2
ax.plot(centres, chi2_density, **ref,
        label=r"$\chi^2_1$")
ax.axvline(threshold, **thr)
ax.set_yscale("log")
ax.set_xlabel(r"$\tilde\lambda$")
ax.set_ylabel("density")
ax.legend()

plt.show()
