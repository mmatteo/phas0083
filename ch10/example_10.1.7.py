# Example 10.1.7 (Figure 10.3): Test statistic of the exponential sample against $\lambda_0$, with the simulated and chi-squared level-0.10 thresholds, and the 90\% confidence interval
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from preamble import *  # imports, rng, colours: see preamble.py

x = np.array([3.54, 5.13, 2.84, 4.48, 1.03, 16.92,
              0.05, 14.05, 2.88, 1.50, 2.71, 1.56])
n = x.size
alpha = 0.10
m = 10_000
lambda_values = np.linspace(2, 12, 26)


# x holds one sample per row
def nlrt(x, lambda_0):
    lambda_hat = x.mean(axis=-1)
    return 2 * n * (np.log(lambda_0 / lambda_hat)
                    + lambda_hat / lambda_0 - 1)


t_obs = nlrt(x, lambda_values)
# find the threshold at each lambda_0
k = round((m + 1) * (1 - alpha)) - 1
threshold = np.zeros_like(lambda_values)
for i, lambda_0 in enumerate(lambda_values):
    x_sim = rng.exponential(scale=lambda_0, size=(m, n))
    T_sorted = np.sort(nlrt(x_sim, lambda_0))
    threshold[i] = T_sorted[k]

# interval: lambda_0 below the chi-squared threshold
grid = np.linspace(2, 12, 2001)
c = chi2.ppf(1 - alpha, df=1)
inside = grid[nlrt(x, grid) <= c]
print(f"MLE {x.mean():.2f}, {1 - alpha:.0%} interval "
      f"[{inside.min():.2f}, {inside.max():.2f}]")

fig, ax = plt.subplots()
ax.plot(lambda_values, t_obs, color=col.like,
        label="test value")
ax.plot(lambda_values, threshold, "x", color=col.draws,
        label="simulated")
ax.axhline(c, color=col.ref, ls="--", label=r"$\chi^2_1$")
ax.set(xlabel=r"$\lambda_0$", ylabel="test statistic")
ax.legend()

plt.show()
