# Example 9.5.1 (Figure 9.10): Bootstrap distribution of the likelihood-ratio statistic under $H_0$ (top) and its survival function (bottom), with the level-0.05 threshold
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from preamble import *  # imports, rng, colours: see preamble.py

# the on/off log-likelihood, up to constant terms; a count
# of zero would give log(0), so a rate of zero is replaced
# by a tiny value
def log_l(x, y, lam, nu, tau):
    nu = max(nu, 1e-12)
    lam = max(lam, 1e-12)
    return (x * np.log(lam + nu) - (lam + nu)
            + y * np.log(tau * nu) - tau * nu)


# -2 log of the likelihood ratio for H0: lambda = 0, with
# the MLEs under H0 and over the whole parameter space
def lrt(x, y, tau):
    if x <= y / tau:
        return 0.0
    nu_0 = (x + y) / (1 + tau)
    nu_hat = y / tau
    lam_hat = x - y / tau
    return -2 * (log_l(x, y, 0.0, nu_0, tau)
                 - log_l(x, y, lam_hat, nu_hat, tau))


tau = 2.0
B = 100_000
alpha = 0.05

# the simulation model under H0: the MLE of nu from the
# observed pair, nu_0_hat = (x + y) / (1 + tau); its value
# here
nu_0_hat = 50
x = rng.poisson(nu_0_hat, size=B)
y = rng.poisson(tau * nu_0_hat, size=B)
T = np.array([lrt(xi, yi, tau) for xi, yi in zip(x, y)])

# the threshold: the (B + 1)(1 - alpha)-th ordered value
T_sorted = np.sort(T)
c = T_sorted[int((B + 1) * (1 - alpha)) - 1]
print(f"threshold for level 0.05: T > {c:.3f}")

fig, axes = plt.subplots(2, 1, sharex=True)
axes[0].hist(T, density=True, bins=40, color=col.hist)
axes[0].set_yscale("log")
axes[0].set_ylabel("density")
survival = np.linspace(1, 0, B, endpoint=False)
axes[1].plot(T_sorted, survival, color=col.cdf)
axes[1].set_ylabel("survival")
axes[1].set_xlabel("$T$")
for ax in axes:
    ax.axvline(c, **thr)

plt.show()
