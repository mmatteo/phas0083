# Example 10.3.1 (Figure 10.6): Test statistic of the observation $x_\mathrm{obs}=1050$ and the bootstrap level-0.10 threshold as functions of $\lambda_0$; the shaded region is the confidence interval
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from preamble import *  # imports, rng, colours: see preamble.py

x_obs = 1050
nu = 1000
lambda_values = np.linspace(0, 120, 61)


def nlrt(x, lambda_0, nu):
    """-2 log likelihood ratio of the on/off model."""
    lambda_hat = np.maximum(0, x - nu)
    return (-2 * poisson.logpmf(x, lambda_0 + nu)
            + 2 * poisson.logpmf(x, lambda_hat + nu))


obs = np.zeros_like(lambda_values)
threshold = np.zeros_like(lambda_values)
for i, lambda_0 in enumerate(lambda_values):
    obs[i] = nlrt(x_obs, lambda_0, nu)
    x_star = poisson.rvs(lambda_0 + nu, size=1_000_000,
                         random_state=rng)
    T = nlrt(x_star, lambda_0, nu)
    threshold[i] = np.quantile(T, 0.9)

fig, ax = plt.subplots()
accepted = obs <= threshold
ax.fill_between(lambda_values, threshold, 0,
                where=accepted, color=col.like, alpha=0.2)
ax.plot(lambda_values, threshold, **thr,
        label="threshold")
ax.plot(lambda_values, obs, color=col.like,
        label="test value")
ax.set_xlabel(r"$\lambda_0$")
ax.set_ylabel("test statistic")
ax.legend()

plt.show()
