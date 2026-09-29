# Survival function of the test statistic under $H_0$, with the threshold for $\alpha=5\%$ and the observed value
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
c = np.quantile(T, 1 - alpha)
t_obs = nlrt(2100, lambda_0, nu)

t = np.linspace(0, T.max(), 2000)
fig, ax = plt.subplots()
ax.plot(t, chi2.sf(t, df=1), color=col.cdf)
for value, style, label in [
        (c, thr, "$c$"),
        (t_obs, dict(color=col.data),
         r"$\tilde\lambda(x_\mathrm{obs})$")]:
    ax.axvline(value, label=label, **style)
    ax.hlines(chi2.sf(value, df=1), 0, value, **style)
ax.set_xlim(0, 6)
ax.set_ylim(0, 0.1)
ax.set_xlabel(r"$\tilde\lambda(x)$")
ax.set_ylabel(r"$1-F$ = p-value")
ax.legend()

plt.show()
