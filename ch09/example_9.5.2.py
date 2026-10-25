# Example 9.5.2 (Figure 9.12): Power of the level-0.05 likelihood-ratio test as a function of the signal $\lambda$
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
nu = 50.0
B = 10_000

# the threshold of the previous example
c = 2.7

# the power at each lambda: the fraction of the simulated
# data sets that the test rejects
lam_values = np.linspace(0, 30, 20)
power = []
for lam in lam_values:
    x = rng.poisson(lam + nu, size=B)
    y = rng.poisson(tau * nu, size=B)
    T = np.array([lrt(xi, yi, tau) for xi, yi in zip(x, y)])
    power.append(np.mean(T > c))

fig, ax = plt.subplots()
ax.plot(lam_values, power, "o-", color=col.emp)
ax.set_xlabel(r"$\lambda$")
ax.set_ylabel("power")

plt.show()
