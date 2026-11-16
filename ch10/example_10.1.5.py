# Example 10.1.5 (Figure 10.2): Test statistic of $x_\mathrm{obs}=2050$ against $\lambda_0$, with the simulated and chi-squared level-0.05 thresholds
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from preamble import *  # imports, rng, colours: see preamble.py

x_obs = 2050
nu = 1000
alpha = 0.05
m = 100_000
lambda_values = np.linspace(900, 1200, 25)


def nlrt(x, lambda_0, nu):
    lambda_hat = np.maximum(0, x - nu)
    return (-2 * poisson.logpmf(x, lambda_0 + nu)
            + 2 * poisson.logpmf(x, lambda_hat + nu))


t_obs = nlrt(x_obs, lambda_values, nu)
# find the threshold at each lambda_0
k = round((m + 1) * (1 - alpha)) - 1
threshold = np.zeros_like(lambda_values)
for i, lambda_0 in enumerate(lambda_values):
    x_sim = rng.poisson(lambda_0 + nu, size=m)
    T_sorted = np.sort(nlrt(x_sim, lambda_0, nu))
    threshold[i] = T_sorted[k]

fig, ax = plt.subplots()
ax.plot(lambda_values, t_obs, color=col.like,
        label="test value")
ax.plot(lambda_values, threshold, "x", color=col.draws,
        label="simulated")
ax.axhline(chi2.ppf(1 - alpha, df=1), color=col.ref,
           ls="--", label=r"$\chi^2_1$")
ax.set(xlabel=r"$\lambda_0$", ylabel="test statistic")
ax.legend()

plt.show()
