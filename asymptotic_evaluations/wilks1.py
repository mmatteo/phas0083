# Bootstrap distribution of the test statistic under $H_0$, the chi-squared prediction and the level-0.05 threshold
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from preamble import *  # imports, rng, colours: see preamble.py

def nlrt(x, lambda_0, nu):
    """-2 log likelihood ratio of the on/off model."""
    lambda_hat = np.maximum(0, x - nu)
    return (-2 * poisson.logpmf(x, lambda_0 + nu)
            + 2 * poisson.logpmf(x, lambda_hat + nu))


lambda_0, nu, alpha = 1000, 1000, 0.05
x_star = rng.poisson(lambda_0 + nu, size=1_000_000)
T = nlrt(x_star, lambda_0, nu)
threshold = np.quantile(T, 1 - alpha)
print(f"level {alpha}: reject if T > {threshold:.3f}")

fig, ax = plt.subplots()
_, bins, _ = ax.hist(T, bins=50, density=True,
                     color=col.hist)
# chi-squared probability of each bin, per unit width
chi2_density = np.diff(chi2.cdf(bins, df=1)) / np.diff(bins)
centres = (bins[:-1] + bins[1:]) / 2
ax.plot(centres, chi2_density, **ref,
        label=r"$\chi^2_1$")
ax.axvline(threshold, **thr)
ax.set_xlim(0, 15)
ax.set_yscale("log")
ax.set_xlabel(r"$\tilde\lambda$")
ax.set_ylabel("density")
ax.legend()

plt.show()
