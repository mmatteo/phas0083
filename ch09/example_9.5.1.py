# Example 9.5.1 (Figure 9.10): Bootstrap distribution of the likelihood-ratio statistic under $H_0$ (top) and its survival function (bottom), with the level-0.05 threshold
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from preamble import *  # imports, rng, colours: see preamble.py

def log_l(x, y, lam, nu, tau):
    """On/off log-likelihood, up to constant terms."""
    nu = nu if nu > 0 else 1e-12
    lam = lam if lam > 0 else 1e-12
    return (x * np.log(lam + nu) - (lam + nu)
            + y * np.log(tau * nu) - tau * nu)


def lrt(x, y, tau):
    """-2 log of the likelihood ratio for H0: lambda = 0."""
    if x <= y / tau:
        return 0.0
    nu_0 = (x + y) / (1 + tau)           # MLE under H0
    # unrestricted MLE
    nu_hat, lam_hat = y / tau, x - y / tau
    return -2 * (log_l(x, y, 0.0, nu_0, tau)
                 - log_l(x, y, lam_hat, nu_hat, tau))


tau, B = 2.0, 100_000
# MLE of nu under H0 from the observed pair (x, y):
# nu_0_hat = (x + y) / (1 + tau); its value here
nu_0_hat = 50
x = rng.poisson(nu_0_hat, size=B)         # under H0
y = rng.poisson(tau * nu_0_hat, size=B)
T = np.array([lrt(xi, yi, tau) for xi, yi in zip(x, y)])
c = np.quantile(T, 1 - 0.05)
print(f"threshold for level 0.05: T > {c:.3f}")

fig, axes = plt.subplots(2, 1, sharex=True)
axes[0].hist(T, density=True, bins=40, color=col.hist)
axes[0].set_yscale("log")
axes[0].set_ylabel("density")
survival = np.linspace(1, 0, B, endpoint=False)
axes[1].plot(np.sort(T), survival, color=col.cdf)
axes[1].set_ylabel("survival")
axes[1].set_xlabel("$T$")
for ax in axes:
    ax.axvline(c, **thr)

plt.show()
