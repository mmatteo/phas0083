# Example 11.6.1 (Figure 11.7): Simulated distribution of the likelihood-ratio statistic under $H_0$ (top) and its ecdf (bottom), with the level-0.05 threshold
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from preamble import *  # imports, rng, colours: see preamble.py

tau = 2.0
m = 100_000
alpha = 0.05

# value of the MLE of nu under H0 for the observed pair
nu_0_hat = 50


def log_l(x, y, lam, nu, tau):
    # a rate of zero would give log(0) for a count of zero
    nu = max(nu, 1e-12)
    lam = max(lam, 1e-12)
    return (x * np.log(lam + nu) - (lam + nu)
            + y * np.log(tau * nu) - tau * nu)


def lrt(x, y, tau):
    if x <= y / tau:
        return 0.0
    nu_0 = (x + y) / (1 + tau)
    nu_hat = y / tau
    lam_hat = x - y / tau
    return -2 * (log_l(x, y, 0.0, nu_0, tau)
                 - log_l(x, y, lam_hat, nu_hat, tau))


x = rng.poisson(nu_0_hat, size=m)
y = rng.poisson(tau * nu_0_hat, size=m)
T = np.array([lrt(xi, yi, tau) for xi, yi in zip(x, y)])

# find the threshold at level alpha
T_sorted = np.sort(T)
c = T_sorted[round((m + 1) * (1 - alpha)) - 1]
print(f"threshold for level {alpha}: T > {c:.3f}")

fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)
ax1.hist(T_sorted, bins=40, density=True, color=col.hist)
ax1.axvline(c, color=col.ref, ls=":")
ax1.set(yscale="log", ylabel="density")
ax2.ecdf(T_sorted, color=col.draws)
ax2.axvline(c, color=col.ref, ls=":")
ax2.set(xlabel="$T$", ylabel="ecdf")

plt.show()
