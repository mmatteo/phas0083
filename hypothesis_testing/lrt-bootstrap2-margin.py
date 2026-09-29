# Power of the level-0.05 likelihood-ratio test as a function of the signal $\lambda$
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


tau, nu, B = 2.0, 50.0, 10_000
c = 2.7  # threshold from the previous example
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
