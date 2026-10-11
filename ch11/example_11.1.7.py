# Example 11.1.7 (Figure 11.3): Test statistic of the exponential sample against $\lambda_0$, with the bootstrap and chi-squared level-0.10 thresholds, and the 90\% confidence interval
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from preamble import *  # imports, rng, colours: see preamble.py

def nlrt(x, lambda_0):
    """-2 log likelihood ratio of the exponential model."""
    lambda_hat = x.mean()
    return 2 * x.size * (np.log(lambda_0 / lambda_hat)
                         + lambda_hat / lambda_0 - 1)


x = np.array([4.808, 4.672, 4.769, 0.559,
              0.172, 2.905, 2.819, 6.248])
alpha, B = 0.10, 10_000
lambda_values = np.linspace(1, 8, 25)
obs = np.array([nlrt(x, l0) for l0 in lambda_values])
threshold = np.zeros_like(lambda_values)
for i, lambda_0 in enumerate(lambda_values):
    x_star = rng.exponential(lambda_0, size=(B, x.size))
    T = np.array([nlrt(b, lambda_0) for b in x_star])
    threshold[i] = np.quantile(T, 1 - alpha)

# the interval: the statistic below the chi2 threshold
grid = np.linspace(1, 8, 2001)
c_chi2 = chi2.ppf(1 - alpha, df=1)
inside = grid[[nlrt(x, l0) <= c_chi2
               for l0 in grid]]
print(f"MLE {x.mean():.2f}, 90% interval "
      f"[{inside.min():.2f}, {inside.max():.2f}]")

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
