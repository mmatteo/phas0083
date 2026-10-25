# Example 11.1.5 (Figure 11.2): Test statistic of $x_\mathrm{obs}=2050$ against $\lambda_0$, with the bootstrap and chi-squared level-0.05 thresholds
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from preamble import *  # imports, rng, colours: see preamble.py

# -2 log likelihood ratio of the on/off model, with the
# MLE of lambda kept at or above zero
def nlrt(x, lambda_0, nu):
    lambda_hat = np.maximum(0, x - nu)
    return (-2 * poisson.logpmf(x, lambda_0 + nu)
            + 2 * poisson.logpmf(x, lambda_hat + nu))


x_obs = 2050
nu = 1000
alpha = 0.05
B = 100_000
lambda_values = np.linspace(900, 1200, 25)
obs = nlrt(x_obs, lambda_values, nu)
# at each lambda_0 the threshold is the
# (B + 1)(1 - alpha)-th ordered value of the B simulated
# values
threshold = np.zeros_like(lambda_values)
for i, lambda_0 in enumerate(lambda_values):
    x_star = rng.poisson(lambda_0 + nu, size=B)
    T_sorted = np.sort(nlrt(x_star, lambda_0, nu))
    threshold[i] = T_sorted[int((B + 1) * (1 - alpha)) - 1]

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
