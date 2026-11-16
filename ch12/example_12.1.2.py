# Example 12.1.2 (Figure 12.2): Survival function of the test statistic under $H_0$, with the threshold for $\alpha=5\%$ and the observed value
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from preamble import *  # imports, rng, colours: see preamble.py

lambda_0 = 1000
nu = 1000
alpha = 0.05
m = 1_000_000
x_obs = 2100


def nlrt(x, lambda_0, nu):
    lambda_hat = np.maximum(0, x - nu)
    return (-2 * poisson.logpmf(x, lambda_0 + nu)
            + 2 * poisson.logpmf(x, lambda_hat + nu))


# simulate the statistic under H0 and find the threshold
x_sim = rng.poisson(lambda_0 + nu, size=m)
T_sorted = np.sort(nlrt(x_sim, lambda_0, nu))
c = T_sorted[round((m + 1) * (1 - alpha)) - 1]
# observed statistic and its p-value
t_obs = nlrt(x_obs, lambda_0, nu)
p_value = chi2.sf(t_obs, df=1)
print(f"threshold {c:.2f}")
print(f"p-value of x_obs={x_obs}: {p_value:.3f}")

u = np.linspace(0, 6, 200)
fig, ax = plt.subplots()
ax.plot(u, chi2.sf(u, df=1), color=col.cdf)
ax.axvline(c, color=col.ref, ls=":", label="$c$")
ax.hlines(chi2.sf(c, df=1), 0, c, color=col.ref, ls=":")
ax.axvline(t_obs, color=col.data,
           label=r"$-2\log\lambda(x_\mathrm{obs})$")
ax.hlines(p_value, 0, t_obs, color=col.data)
ax.set(xlim=(u[0], u[-1]), ylim=(0, 0.1))
ax.set_xlabel(r"$-2\log\lambda(x)$")
ax.set_ylabel(r"$1-F$ = p-value")
ax.legend()

plt.show()
