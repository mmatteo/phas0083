# Example 11.3.3 (Figure 11.9): Sample of 60 values from the peak-over-background model, with $\hat\mu$ and its 90\% confidence interval
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from preamble import *  # imports, rng, colours: see preamble.py

x = np.concatenate([rng.normal(0.5, 1, 40),
                    rng.uniform(-4, 4, 20)])
sigma = 1.0
alpha = 0.10


# the likelihood-ratio statistic for the mean of a normal
# sample with known sigma
def nlrt(mu_0, x, sigma):
    return x.size * ((x.mean() - mu_0) / sigma)**2


# the interval: the values of mu_0 at which the statistic
# stays below the chi-squared threshold
mu_hat = x.mean()
mu_grid = np.linspace(mu_hat - 3, mu_hat + 3, 1000)
T = nlrt(mu_grid, x, sigma)
inside = mu_grid[T <= chi2.ppf(1 - alpha, df=1)]
low = inside.min()
high = inside.max()
print(f"mu_hat = {mu_hat:.2f}, I = [{low:.2f}, {high:.2f}]")

fig, ax = plt.subplots()
ax.hist(x, color=col.hist)
ax.axvline(mu_hat, color=col.data,
           label=r"$\hat\mu$")
ax.axvline(low, **thr, label="$I$")
ax.axvline(high, **thr)
ax.set_xlabel("$x$")
ax.set_ylabel("counts")
ax.legend()

plt.show()
