# Example 11.1.7 (Figure 11.3): Test statistic of the exponential sample against $\lambda_0$, with the bootstrap and chi-squared level-0.10 thresholds, and the 90\% confidence interval
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from preamble import *  # imports, rng, colours: see preamble.py

x = np.array([3.54, 5.13, 2.84, 4.48, 1.03, 16.92,
              0.05, 14.05, 2.88, 1.50, 2.71, 1.56])
alpha = 0.10
B = 10_000
lambda_values = np.linspace(2, 12, 26)


# -2 log likelihood ratio of the exponential model, with
# the MLE of lambda the sample mean
def nlrt(x, lambda_0):
    lambda_hat = x.mean()
    return 2 * x.size * (np.log(lambda_0 / lambda_hat)
                         + lambda_hat / lambda_0 - 1)


obs = nlrt(x, lambda_values)
# at each lambda_0 the threshold is the
# (B + 1)(1 - alpha)-th ordered value of the statistic of
# B simulated samples
threshold = np.zeros_like(lambda_values)
for i, lambda_0 in enumerate(lambda_values):
    T = np.zeros(B)
    for b in range(B):
        x_star = rng.exponential(lambda_0, size=x.size)
        T[b] = nlrt(x_star, lambda_0)
    T_sorted = np.sort(T)
    threshold[i] = T_sorted[int((B + 1) * (1 - alpha)) - 1]

# the interval: the values of lambda_0 at which the
# statistic stays below the chi-squared threshold
grid = np.linspace(2, 12, 2001)
c_chi2 = chi2.ppf(1 - alpha, df=1)
inside = grid[nlrt(x, grid) <= c_chi2]
print(f"MLE {x.mean():.2f}, 90% interval "
      f"[{inside.min():.2f}, {inside.max():.2f}]")

fig, ax = plt.subplots()
ax.plot(lambda_values, obs, color=col.like,
        label="test value")
ax.plot(lambda_values, threshold, "x", color=col.thr,
        label="bootstrap")
ax.axhline(c_chi2, **ref, label=r"$\chi^2_1$")
ax.set_xlabel(r"$\lambda_0$")
ax.set_ylabel("test statistic")
ax.legend()

plt.show()
