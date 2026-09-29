# Test statistic of $x_\mathrm{obs}=2050$ against $\lambda_0$, with the bootstrap and chi-squared level-0.05 thresholds
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from preamble import *  # imports, rng, colours: see preamble.py

def nlrt(x, lambda_0, nu):
    """-2 log likelihood ratio of the on/off model."""
    lambda_hat = np.maximum(0, x - nu)
    return (-2 * poisson.logpmf(x, lambda_0 + nu)
            + 2 * poisson.logpmf(x, lambda_hat + nu))


x_obs, nu, alpha = 2050, 1000, 0.05
lambda_values = np.linspace(900, 1200, 25)
obs = np.zeros_like(lambda_values)
threshold = np.zeros_like(lambda_values)
for i, lambda_0 in enumerate(lambda_values):
    obs[i] = nlrt(x_obs, lambda_0, nu)
    x_star = rng.poisson(lambda_0 + nu, size=100_000)
    T = nlrt(x_star, lambda_0, nu)
    threshold[i] = np.quantile(T, 1 - alpha)

fig, ax = plt.subplots()
ax.plot(lambda_values, obs, color=col.like,
        label="test value")
ax.plot(lambda_values, threshold, "x", color=col.thr,
        label="bootstrap")
ax.axhline(chi2.ppf(1 - alpha, df=1), **ref,
           label=r"$\chi^2_1$")
ax.set_xlabel(r"$\lambda_0$")
ax.set_ylabel("test statistic")
ax.legend()

plt.show()
