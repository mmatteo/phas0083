# Example 10.3.2 (Figure 10.7): Test statistic of four observations and the bootstrap level-0.10 threshold as functions of $\lambda_0$
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from preamble import *  # imports, rng, colours: see preamble.py

x_obs = np.array([990, 1000, 1050, 1100])
nu = 1000
lambda_values = np.linspace(0, 200, 101)


def nlrt(x, lambda_0, nu):
    """-2 log likelihood ratio of the on/off model."""
    lambda_hat = np.maximum(0, x - nu)
    return (-2 * poisson.logpmf(x, lambda_0 + nu)
            + 2 * poisson.logpmf(x, lambda_hat + nu))


obs = np.zeros((x_obs.size, lambda_values.size))
threshold = np.zeros_like(lambda_values)
for i, lambda_0 in enumerate(lambda_values):
    obs[:, i] = nlrt(x_obs, lambda_0, nu)
    x_star = poisson.rvs(lambda_0 + nu, size=1_000_000,
                         random_state=rng)
    T = nlrt(x_star, lambda_0, nu)
    threshold[i] = np.quantile(T, 0.9)

fig, ax = plt.subplots()
ax.plot(lambda_values, threshold, **thr,
        label="threshold")
colors = shades(col.like, 4)
for color, x, values in zip(colors, x_obs, obs):
    ax.plot(lambda_values, values, color=color,
            label=rf"$x_\mathrm{{obs}}={x}$")
ax.set_ylim(-0.5, 6)
ax.set_xlabel(r"$\lambda_0$")
ax.set_ylabel("test statistic")
ax.legend()

plt.show()
