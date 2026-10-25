# Example 12.1.2 (Figure 12.2): Survival function of the test statistic under $H_0$, with the threshold for $\alpha=5\%$ and the observed value
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from preamble import *  # imports, rng, colours: see preamble.py

# -2 log likelihood ratio of the on/off model, with the
# MLE of lambda kept at or above zero
def nlrt(x, lambda_0, nu):
    lambda_hat = np.maximum(0, x - nu)
    return (-2 * poisson.logpmf(x, lambda_0 + nu)
            + 2 * poisson.logpmf(x, lambda_hat + nu))


lambda_0 = 1000
nu = 1000
alpha = 0.05
B = 1_000_000
x_obs = 2100

# the simulated statistic under H0 and the threshold, the
# (B + 1)(1 - alpha)-th ordered value
x_star = rng.poisson(lambda_0 + nu, size=B)
T_sorted = np.sort(nlrt(x_star, lambda_0, nu))
c = T_sorted[int((B + 1) * (1 - alpha)) - 1]
# the observed statistic and its p-value from the
# chi-squared survival function
t_obs = nlrt(x_obs, lambda_0, nu)
p_value = chi2.sf(t_obs, df=1)
print(f"threshold {c:.2f}")
print(f"p-value of x_obs={x_obs}: {p_value:.3f}")

t = np.linspace(0, T_sorted.max(), 2000)
fig, ax = plt.subplots()
ax.plot(t, chi2.sf(t, df=1), color=col.cdf)
ax.axvline(c, label="$c$", **thr)
ax.hlines(chi2.sf(c, df=1), 0, c, **thr)
ax.axvline(t_obs, color=col.data,
           label=r"$\tilde\lambda(x_\mathrm{obs})$")
ax.hlines(p_value, 0, t_obs, color=col.data)
ax.set_xlim(0, 6)
ax.set_ylim(0, 0.1)
ax.set_xlabel(r"$\tilde\lambda(x)$")
ax.set_ylabel(r"$1-F$ = p-value")
ax.legend()

plt.show()
